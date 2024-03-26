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

base_url = settings.CLOUDINARY_BASE[0]
# Create your views here.

def view_results(request):
    if request.GET:
        if 'view_category' in request.GET:
            view = "view_category=" + request.GET['view_category']
            values = request.GET['view_category'].split(',')
            type =  values[0]
            if len(values)>1:                
                category = values[1]
                search_term = None
                if type == "cheese":
                    category = get_object_or_404 (CheeseCategory, name=category)
                    product_list = Product.objects.filter(cheese_category=category.id)
                else:
                    category = get_object_or_404 (BeerCategory, name=category) 
                    product_list = Product.objects.filter(beer_category=category.id)   
            else:
                product_list = Product.objects.filter(product_type=type)
                category = None
                search_term = type
        if 'category' in request.GET:
            view = "category=" + request.GET['category']
            values = request.GET['category'].split(',')
            type =  values[0]
            if len(values)>1:                
                category = values[1]
                search_term = None
                if type == "cheese":
                    product_list = Product.objects.filter(cheese_category=category)
                    category = get_object_or_404 (CheeseCategory, pk=category)
                else:
                    product_list = Product.objects.filter(beer_category=category)
                    category = get_object_or_404 (BeerCategory, pk=category)            
            else:
                product_list = Product.objects.filter(product_type=type)
                category = None
                search_term = type
        if 'query' in request.GET:
            products = Product.objects.all()
            view = "query=" + request.GET['query']
            query = request.GET['query'].strip()        
            if query:
                queries = Q(
                    product_number__iexact=query
                    ) | Q(
                        name__icontains=query
                        ) | Q(
                            variety__icontains=query
                            )
                product_list = list(products.filter(queries))
                search_term = query
                cheese_index = []
                cheese_query = Q(name__icontains=query)                
                cheese_categories = list(CheeseCategory.objects.all().filter(cheese_query))
                for category in cheese_categories:
                    cheese_index.append(category.id)
                for i in cheese_index:
                    index_query= Q(
                        cheese_category__exact=i
                    )                    
                    product = list(Product.objects.all().filter(index_query))
                    product_list.extend(product)
                beer_index = []
                beer_query = Q(name__icontains=query)
                beer_categories = list(BeerCategory.objects.all().filter(beer_query))
                for category in beer_categories:
                    beer_index.append(category.id)
                for i in beer_index:
                    index_query= Q(
                        beer_category__exact=i
                    )                    
                    product = list(Product.objects.all().filter(index_query))
                    product_list.extend(product)
            else:
                search_term = "all products"
                product_list = products
            category = None
            type = None
    else:
        product_list = Product.objects.all()
        search_term = "all products"
        category = None
        type = None
        view = None
    number = len(product_list)
    if number==1:
      result = "result"
    else:
      result = "results"
    template = 'product_views/view-products.html'
    context = {
        'current_view': view,
        'base_url' : base_url,
        'number': number,
        'search_term': search_term,
        'products' : product_list,
        'category' : category,
        'result' : result,
        'type' : type
    }
    return render(request, template, context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.product_type == "beer":
        category = get_object_or_404(BeerCategory, name=product.beer_category)
        category_pairs = category.cheese.all()
        pairings = []
        for category in category_pairs:
            pairings.extend(list(Product.objects.filter(cheese_category=category.id)))
    else:
        category = get_object_or_404(CheeseCategory, name=product.cheese_category)
        category_pairs = category.pairs_with.all()
        pairings = []
        for category in category_pairs:
            pairings.extend(list(Product.objects.filter(beer_category=category.id)))
    template = 'product_views/product-detail.html'
    context = {
        'base_url' : base_url,
        'product': product,
        'pairings': pairings,
    }
    return render(request, template, context)