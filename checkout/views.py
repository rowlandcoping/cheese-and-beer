from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from datetime import datetime, timedelta
from .models import Order, OrderItems
from django.contrib.auth.models import User
from addresses.models import Addresses
from products.models import Product
from addresses.forms import AddressForm
from basket.contexts import basket_total
from django.db.models import Sum
import stripe
import json


def checkout(request):
    """
    Loads the checkout page, also processes orders on checkout form submission
    On load the page updates any existing payment intent, or creates a new one.
    It also sends the correct address to the view (selected, default or none).
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    basket = request.session.get('basket', {})
    current_basket = basket_total(request)
    selected_address = request.session.get('selected_address', {})
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            if request.user.is_authenticated:
                user_id = request.user
                address_id = Addresses.objects.get(
                    postcode=request.POST.get('postcode'))
            else:
                user_check = User.objects.all()
                for check in user_check:
                    if check.email == request.POST.get('order_email'):
                        user_id = check
                    else:
                        user_id = None
                address_id = None
            time_created = datetime.now()
            delivery_date = datetime.now() + timedelta(days=5)
            stripe_pid = request.POST.get('client_secret').split('_secret')[0]
            order = Order.objects.create(
                user_id=user_id,
                shipping_id=address_id,
                email=request.POST.get('order_email'),
                full_name=request.POST.get('full_name'),
                address_line_one=request.POST.get('address_line_one'),
                address_line_two=request.POST.get('address_line_two'),
                town_or_city=request.POST.get('town_or_city'),
                county=request.POST.get('county'),
                postcode=request.POST.get('postcode'),
                order_date=time_created,
                delivery_date=delivery_date,
                items_total=current_basket['basket_total'],
                delivery_cost=current_basket['delivery_charge'],
                grand_total=current_basket['grand_total'],
                stripe_pid=stripe_pid,
            )
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItems(
                            order_id=order,
                            product_type=product.product_type,
                            product=product,
                            price=product.price,
                            quantity=item_data,
                        )
                        order_item.save()
                        units_sold = OrderItems.objects.filter(
                            product=product).aggregate(Sum('quantity'))
                        Product.objects.filter(pk=product.id).update(
                            units_sold=units_sold['quantity__sum']
                        )
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your "
                        "basket wasn't found in our database. "
                        "Please contact us for assistance.")
                    )
                    order.delete()
                    return redirect('contact_form')
        if 'basket' in request.session:
            del request.session['basket']
        if 'intent_id' in request.session:
            del request.session['intent_id']
        if 'selected_address' in request.session:
            del request.session['selected_address']
        return redirect(reverse('confirmation', args=[order.order_number]))
    if not basket:
        return redirect('home')
    if request.user.is_authenticated:
        addresses = Addresses.objects.filter(
            user_id=request.user.id).order_by('-default', 'id')
        if addresses:
            if selected_address:
                address = get_object_or_404(
                    addresses, postcode=selected_address['postcode'],
                    address_line_one=selected_address['address_line_one'])
                email = request.user.email
            else:
                address = get_object_or_404(addresses, default=True)
                email = request.user.email
        else:
            address = None
            email = request.user.email
    else:
        addresses = None
        address = None
        email = ""
    stripe.api_key = stripe_secret_key
    current_basket = basket_total(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    intent_id = request.session.get('intent_id', {})
    if address:
        address_id = address.id
    else:
        address_id = None
    if intent_id:
        client_secret = intent_id['secret']
        pid = client_secret.split('_secret')[0]
        existing_order = Order.objects.filter(stripe_pid=pid)
        if existing_order:
            if 'basket' in request.session:
                del request.session['basket']
            if 'intent_id' in request.session:
                del request.session['intent_id']
            if 'selected_address' in request.session:
                del request.session['selected_address']
            messages.error(request, (
                        "Your order has already been processed\n"
                        "Please check your order history.")
                    )
            return redirect('home')
        else:
            stripe.PaymentIntent.modify(pid, amount=stripe_total, metadata={
                'basket': json.dumps(request.session.get('basket', {})),
                'username': request.user,
                'address_id': address_id,
                'items_total': current_basket['basket_total'],
                'delivery_cost': current_basket['delivery_charge'],
            })
    else:
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            metadata={
                'basket': json.dumps(request.session.get('basket', {})),
                'username': request.user,
                'address_id': address_id,
                'items_total': current_basket['basket_total'],
                'delivery_cost': current_basket['delivery_charge'],
            }
        )
        intent_id = request.session.get('intent_id', {})
        intent_id['secret'] = intent.client_secret
        request.session['intent_id'] = intent_id
        client_secret = intent.client_secret
    template = 'checkout/checkout.html'
    if address is not None:
        address_form = AddressForm(instance=address)
    else:
        address_form = AddressForm()
    context = {
        'user_addresses': addresses,
        'user_email': email,
        'address': address,
        'order_info': current_basket,
        'address_form': address_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }
    return render(request, template, context)


def confirmation(request, order_number):
    """
    On sucessful checkout redirects the user to the order confirmation page.
    It passes the order number so the user can review their order.
    """
    order = get_object_or_404(Order, order_number=order_number)
    template = 'checkout/confirmation.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
