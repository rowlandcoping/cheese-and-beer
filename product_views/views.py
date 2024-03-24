from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from products.models import CheeseCategory, BeerCategory, Product
import uuid
import io
import re
import cloudinary
import cloudinary.uploader
import PIL
from PIL import Image
import decimal

# Create your views here.

def view_results(request):
    if request.GET:
        if 'category' in request.GET:
            values = request.GET['category'].split(',')
            type =  values[0]
            if len(values)>1:                
                category = values[1]
                search_term = None
                if type == "cheese":
                    products = Product.objects.filter(cheese_category=category)
                    category = get_object_or_404 (CheeseCategory, pk=category)
                else:
                    products = Product.objects.filter(beer_category=category)
                    category = get_object_or_404 (BeerCategory, pk=category)            
            else:
                products = Product.objects.filter(product_type=type)
                category = None
                search_term = type
    else:
        products = Product.objects.all()
    number = products.count()
    if number==1:
        result = "result"
    else:
        result = "results"
    base_url = settings.CLOUDINARY_BASE[0]
    template = 'product_views/view-products.html'
    context = {
        'base_url' : base_url,
        'number': number,
        'search_term': search_term,
        'products' : products,
        'category' : category,
        'result' : result,
        'type' : type
    }
    return render(request, template, context)