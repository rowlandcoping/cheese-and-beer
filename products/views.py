from django.shortcuts import render, redirect
from django.urls import reverse
from .models import CheeseCategory
from .forms import CheeseCategoryForm, BeerCategoryForm
import os
import io
import cloudinary
import cloudinary.uploader
import PIL
from PIL import Image



# Create your views here.

cloudinary.config(
    cloud_name=os.environ.get('CLOUD_NAME'),
    api_key=os.environ.get('API_KEY'),
    api_secret=os.environ.get('API_SECRET'))

def imageConvert(image, width, quality, format):
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
    """ Returns form to add a cheese category"""

    if request.method=='POST':
        ImageUpload = request.FILES.get('image')
        name = request.POST.get('name')
        image_url = str(name + "-image")
        image_alt = str("An image of " + name + " cheese")
        converted_image = imageConvert(
                                ImageUpload, 400, 75, "webp")
        cloudinary.uploader.upload(
                                converted_image,
                                public_id=image_url, folder="cheese-and-beer/cheese-categories")
        form = CheeseCategoryForm(request.POST)
        if form.is_valid():
            CheeseCategory.objects.create(
                name=name, 
                description=request.POST.get('description'), 
                image_url=image_url,
                image_alt=image_alt
            )
            return redirect(reverse(add_cheese_category))
        else:
            return redirect(admin_console)
    form = CheeseCategoryForm()
    template = 'products/add-cheese-category.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

def add_beer_category(request):
    """ Returns form to add a cheese category"""

    beer_form = BeerCategoryForm()
        
    template = 'products/add-beer-category.html'
    context = {
        'form': beer_form,
    }

    return render(request, template, context)