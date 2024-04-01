from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from datetime import datetime
from addresses.models import Addresses
from addresses.forms import AddressForm
from basket.contexts import basket_total
import uuid
import io
import re
import cloudinary
import cloudinary.uploader
import PIL
from PIL import Image
import decimal


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
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    basket = request.session.get('basket', {})
    if not basket:
        return redirect('home')
    current_basket = basket_total(request)
    total = current_basket['basket_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
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
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)