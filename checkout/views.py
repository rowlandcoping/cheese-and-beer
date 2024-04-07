from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.http import require_POST
from datetime import datetime, timedelta
from .models import Order, OrderItems
from addresses.models import Addresses
from products.models import Product
from addresses.forms import AddressForm
from basket.contexts import basket_total
import stripe
import json





@require_POST
def cache_checkout_data(request):
    try:
        # gets ths data from the body of the fetch request and converts to python dictionary
        json_data = json.loads(request.body)
        # retrieves pid
        pid = json_data['client_secret'].split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # updates payment intent with final info
        stripe.PaymentIntent.modify(pid, metadata={
           'basket': json.dumps(request.session.get('basket', {})),
           'username': request.user,
        })
        # lets fetch request know the request has been carried out.
        print("you have reached this")
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)
    

def checkout(request):    
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    basket = request.session.get('basket', {})
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            if request.user.is_authenticated:
                user_id = request.user
                address_id = Addresses.objects.get(postcode=request.POST.get('postcode'))                 
            else:
                user_id = None
                address_id = None                              
            current_basket = basket_total(request)
            time_created = datetime.now()
            delivery_date = datetime.now() + timedelta(days=5)
            order = Order.objects.create(
                user_id = user_id,
                shipping_id = address_id,
                email = request.POST.get('order_email'),
                full_name = request.POST.get('full_name'),
                address_line_one = request.POST.get('address_line_one'),
                address_line_two = request.POST.get('address_line_two'),
                town_or_city = request.POST.get('town_or_city'),
                county = request.POST.get('county'),
                postcode = request.POST.get('postcode'),
                order_date = time_created,
                delivery_date = delivery_date,
                items_total = current_basket['basket_total'],
                delivery_cost = current_basket['delivery_charge'],
                grand_total = current_basket['grand_total'],
                stripe_pid = request.POST.get('client_secret').split('_secret')[0],
            )
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItems(
                            order_id=order,
                            product_type = product.product_type,
                            product=product,
                            price=product.price,
                            quantity=item_data,
                        )
                        order_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect('home')
        if 'basket' in request.session:
            del request.session['basket']
        if 'intent_id' in request.session:
            del request.session['intent_id']
        return redirect('home')
    
    if not basket:
        return redirect('home')
    current_basket = basket_total(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    intent_id = request.session.get('intent_id', {})
    if intent_id:
        client_secret = intent_id['secret']
        pid = client_secret.split('_secret')[0]
        stripe.PaymentIntent.modify(pid, amount=stripe_total, metadata={
           'basket': json.dumps(request.session.get('basket', {})),
           'username': request.user,
        })
    else:
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        intent_id = request.session.get('intent_id', {})
        intent_id['secret'] = intent.client_secret
        request.session['intent_id'] = intent_id
        client_secret = intent.client_secret

    if request.user.is_authenticated:
        addresses = Addresses.objects.filter(user_id=request.user.id)
        if addresses:
            address = get_object_or_404(addresses, default=True)
            email = request.user.email
        else:
            address = None
            email = request.user.email
    else:
        address = None
        email = ""
    template = 'checkout/checkout.html'
    if address is not None:
        address_form = AddressForm(instance=address)
    else:
        address_form = AddressForm()
    context = {
        'user_email': email,
        'address': address,
        'order_info': current_basket,
        'address_form': address_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, template, context)