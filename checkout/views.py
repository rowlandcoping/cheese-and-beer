from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
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

base_url = settings.CLOUDINARY_BASE[0]

def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket the moment")
        return redirect(reverse('products'))

    current_basket = basket_total(request)
    total = current_basket['basket_total']
    #stripe_total = round(total * 100)
    #stripe.api_key = stripe_secret_key
    #intent = stripe.PaymentIntent.create(
    #    amount=stripe_total,
    #    currency=settings.STRIPE_CURRENCY,
    #)

    if request.user.is_authenticated:
        addresses = Addresses.objects.filter(user_id=request.user.id)
        address = get_object_or_404(addresses, default=True)
        email = request.user.email
    else:
        address = None
        email = ""


    #if not stripe_public_key:
    #    messages.warning(request, 'Stripe public key is missing. \
     #       Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    if address:
        address_form = AddressForm(instance=address)
    else:
        address_form = AddressForm()
    context = {
        'user_email': email,
        'base_url': base_url,
        'address': address,
        'order_info': current_basket,
        'address_form': address_form,
        #'stripe_public_key': stripe_public_key,
        #'client_secret': intent.client_secret,
    }

    return render(request, template, context)