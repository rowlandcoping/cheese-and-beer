from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
from datetime import datetime
from .models import CheeseCategory, BeerCategory
from .forms import CheeseCategoryForm, BeerCategoryForm
import io
import re
import cloudinary
import cloudinary.uploader
import PIL
from PIL import Image

def imageConvert(image, width, quality, format):
    """ 
    Converts image format, compresses, resizes 
    and returns in a byte array uploadable to Cloudinary.

    Please note with DRY principles in mind this function has been 
    re-used from my previous project, 'Hopes and Dreams'.
    """
    with Image.open(image) as img:
        img = Image.open(image)
    img_byte_arr = io.BytesIO()
    wpercent = (width/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((width, hsize), PIL.Image.LANCZOS)
    img.save(img_byte_arr, format, optimize=True, quality=quality)
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr


def add_cheese_category(request):
    """
    Returns form to add a cheese category, 
    adds new cheese category to database
    """
    if request.method=='POST':
        name = request.POST.get('name').lower()
        ImageUpload = request.FILES.get('image')
        if ImageUpload:    
            image_url = str(
                re.sub(
                    "[.!# $%;@&'*+/=?^_` {|}~]",
                    "-",
                    name
                    ) + "-image"
                )
            image_alt = str("An image of " + name + " cheese")
            converted_image = imageConvert(
                ImageUpload, 400, 75, "webp")
            cloudinary.uploader.upload(
                converted_image,
                public_id=image_url,
                folder="cheese-and-beer/cheese-categories")
        else:
            image_url = ""
            image_alt = ""
        form = CheeseCategoryForm(request.POST)
        if form.is_valid():
            CheeseCategory.objects.create(
                name=name, 
                description=request.POST.get('description'), 
                image_url=image_url,
                image_alt=image_alt
            )
            return redirect(reverse(add_cheese_category))
    form = CheeseCategoryForm()
    template = 'products/add-cheese-category.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def add_beer_category(request):
    """ 
    Returns form to add a beer category,
    adds new beer category to database
    """
    if request.method=='POST':
        ImageUpload = request.FILES.get('image')
        name = request.POST.get('name')
        if ImageUpload:    
            image_url = str(
                re.sub(
                    "[.!# $%;@&'*+/=?^_` {|}~]",
                    "-",
                    name
                    ) + "-image"
                )
            image_alt = str("An image depicting some " + name)
            converted_image = imageConvert(
                ImageUpload, 400, 75, "webp")
            cloudinary.uploader.upload(
                converted_image,
                public_id=image_url,
                folder="cheese-and-beer/beer-categories")
        else:
            image_url = ""
            image_alt = ""
        form = BeerCategoryForm(request.POST)
        if form.is_valid():
            BeerCategory.objects.create(
                name=name, 
                description=request.POST.get('description'), 
                image_url=image_url,
                image_alt=image_alt
            )
            return redirect(reverse(add_beer_category))
    beer_form = BeerCategoryForm()        
    template = 'products/add-beer-category.html'
    context = {
        'form': beer_form,
    }

    return render(request, template, context)


def edit_categories(request):
    """ 
    Returns a list of categories so that they can be edited
    """
    cheese_categories = CheeseCategory.objects.all()
    beer_categories = BeerCategory.objects.all()
    template = 'products/edit-categories.html'
    context = {
        'cheese_categories': cheese_categories,
        'beer_categories': beer_categories
    }
    return render(request, template, context)

def edit_cheese_category(request, category_id):
    """ 
    Allows user to edit individual cheese category
    """
    if request.method=='POST':
        form = CheeseCategoryForm(request.POST)
        if form.is_valid():
            category = get_object_or_404(CheeseCategory, pk=category_id)
            print(category.image_url)
            # updates image, name and description
            name = request.POST.get('name').lower()
            ImageUpload = request.FILES.get('image')
            image_id = str(datetime.now().timestamp()).split('.')[1]
            if ImageUpload:    
                image_url = str(
                    re.sub(
                        "[.!# $%;@&'*+/=?^_` {|}~]",
                        "-",
                        name
                        ) + "-" + image_id
                    )
                image_alt = str("An image of " + name + " cheese")
                converted_image = imageConvert(
                    ImageUpload, 400, 75, "webp")
                if category.image_url != "":
                    cloudinary.uploader.destroy(
                        "cheese-and-beer/cheese-categories/" + category.image_url)
                cloudinary.uploader.upload(
                    converted_image,
                    public_id=image_url,
                    folder="cheese-and-beer/cheese-categories")                
            else:
                image_url = category.image_url
                image_alt = category.image_alt        
            CheeseCategory.objects.filter(pk=category_id).update(
                name=request.POST.get('name'), 
                description=request.POST.get('description'), 
                image_url=image_url,
                image_alt=image_alt
            )
            # updates many to many pairings based on category buttons selected
            pairings = category.pairs_with.all()
            initial_pairings = list(pairings.values_list('id', flat=True))
            pairings_to_add = []
            pairings_to_remove = []
            if request.POST.get('pairings'):
                pairings_list = request.POST.get('pairings')[:-1]
                updated_pairings = list(pairings_list.split(','))
                updated_pairings = [ int(x) for x in updated_pairings ]            
                if initial_pairings:
                    for pairing in initial_pairings:
                        if pairing not in updated_pairings:
                            pairings_to_remove.append(pairing)
                    for next_pairing in updated_pairings:
                        if next_pairing not in initial_pairings:                   
                            pairings_to_add.append(next_pairing)
                else:
                    for next_pairing in updated_pairings:
                        pairings_to_add.append(next_pairing)
            elif initial_pairings:
                for pairing in initial_pairings:
                    pairings_to_remove.append(pairing)
            if pairings_to_add:
                for add_pairing in pairings_to_add:
                    beer_to_add = get_object_or_404(BeerCategory, pk=add_pairing)
                    category.pairs_with.add(beer_to_add)
            if pairings_to_remove:
                for remove_pairing in pairings_to_remove:
                    beer_to_remove = get_object_or_404(BeerCategory, pk=remove_pairing)
                    category.pairs_with.remove(beer_to_remove)
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')  
    # returns updated data
    base_url = settings.CLOUDINARY_BASE[0]
    category = get_object_or_404(CheeseCategory, pk=category_id)
    pairings = category.pairs_with.all()
    initial_pairings = pairings.values_list('id', flat=True)
    beer_categories = BeerCategory.objects.all()
    form = CheeseCategoryForm(instance=category)
    template = 'products/edit-cheese-category.html'
    context = {
        'initial_pairings': list(initial_pairings),
        'base_url': base_url,
        'form': form,
        'category': category,
        'beer_categories': beer_categories
    }
    return render(request, template, context)


def edit_beer_category(request, category_id):
    """ 
    Allows user to edit individual beer category
    """
    base_url = settings.CLOUDINARY_BASE[0]
    category = get_object_or_404(BeerCategory, pk=category_id)
    pairings = category.cheese.all()
    initial_pairings = pairings.values_list('id', flat=True)
    cheese_categories = CheeseCategory.objects.all()
    form = BeerCategoryForm(instance=category)
    template = 'products/edit-beer-category.html'
    context = {
        'initial_pairings': list(initial_pairings),
        'base_url': base_url,
        'form': form,
        'category': category,
        'cheese_categories': cheese_categories,
    }
    return render(request, template, context)