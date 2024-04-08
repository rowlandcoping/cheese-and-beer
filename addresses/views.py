from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from .models import Addresses
from .forms import AddressForm
from basket.contexts import basket_total
from django.views.decorators.http import require_POST
import uuid
import io
import re
import cloudinary
import cloudinary.uploader
import PIL
from PIL import Image
import decimal

# Create your views here.

def manage_addresses(request):
    template = 'checkout/checkout.html'
    
    context = {
        
    }

    return render(request, template, context)

@require_POST
def add_address(request):
    form = AddressForm(request.POST)
    if request.POST.get('origin') == "checkout":
        return_url="checkout"
    if form.is_valid():
        final_form = form.save(commit=False)  
        final_form.user_id = request.user
        if request.POST.get('default'):
            final_form.default = True                 
        if request.POST.get('selected'):
            selected_address = {}   
            selected_address['postcode'] = form.cleaned_data["postcode"]
            selected_address['address_line_one'] = form.cleaned_data["address_line_one"]
            request.session['selected_address'] = selected_address        
        final_form.save()           
    else:
        messages.error(request, 'Sorry, your address was not added, please try again.')    
    return redirect(return_url)


@require_POST
def select_address(request):
    if 'selected_address' in request.session:
        del request.session['selected_address']
    id = request.POST.get('address_selector')
    address = get_object_or_404(Addresses, pk=id)
    selected_address = {}   
    selected_address['postcode'] = address.postcode
    selected_address['address_line_one'] = address.address_line_one
    request.session['selected_address'] = selected_address
    return redirect('checkout')