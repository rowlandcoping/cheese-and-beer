from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from .models import Addresses
from .forms import AddressForm
from basket.contexts import basket_total
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

def add_address(request):
    form = AddressForm(request.POST)
    if request.POST.get('origin') == "checkout":
        return_url="checkout"
    if form.is_valid():
        final_form = form.save(commit=False)
        if request.POST.get('default'):
            final_form.default = True
    final_form.user_id = request.user
    final_form.save()
    return redirect(return_url)