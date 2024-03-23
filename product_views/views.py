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
            print(type)
            category = values[1]
            print(category)
            if type == "cheese":
                products = Product.objects.filter(cheese_category=category)
                category = get_object_or_404 (CheeseCategory, pk=category)
            else:
                products = Product.objects.filter(beer_category=category)
                category = get_object_or_404 (BeerCategory, pk=category)
    else:
        products = Product.objects.all()
    number = products.count()
    template = 'product_views/view-products.html'
    context = {
        'number': number,
        'type': type,
        'products' : products,
        'category' : category,
    }
    return render(request, template, context)