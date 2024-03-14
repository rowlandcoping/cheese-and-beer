from django.shortcuts import render, redirect
from django.urls import reverse
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