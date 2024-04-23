from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from .models import CheeseCategory, BeerCategory, Product
from .forms import CheeseCategoryForm, BeerCategoryForm, CheeseForm, BeerForm
import uuid
import io
import re
import cloudinary
import cloudinary.uploader
import PIL
from PIL import Image
import decimal


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
    if request.method == 'POST':
        name = request.POST.get('name').lower()
        cat_test = CheeseCategory.objects.all()
        for test in cat_test:
            if name == test.name:
                messages.error(
                    request, "This category already exists, please try again")
                return redirect('add_cheese_category')
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
                folder="cheese-and-beer/products")
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
            messages.success(request, 'Cheese Category Added')
            return redirect('admin_console')
    if request.user.is_superuser:
        form = CheeseCategoryForm()
        template = 'products/add-cheese-category.html'
        context = {
            'form': form,
        }
        return render(request, template, context)
    else:
        return redirect('home')


def add_beer_category(request):
    """
    Returns form to add a beer category,
    adds new beer category to database
    """
    if request.method == 'POST':
        cat_test = BeerCategory.objects.all()
        name = request.POST.get('name').lower()
        for test in cat_test:
            if name == test.name:
                messages.error(
                    request, "This category already exists, please try again")
                return redirect('add_beer_category')
        ImageUpload = request.FILES.get('image')
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
                folder="cheese-and-beer/products")
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
            messages.success(request, 'Beer Category Added')
            return redirect('admin_console')
    if request.user.is_superuser:
        beer_form = BeerCategoryForm()
        template = 'products/add-beer-category.html'
        context = {
            'form': beer_form,
        }

        return render(request, template, context)
    else:
        return redirect('home')


def edit_categories(request):
    """
    Returns a list of categories so that they can be edited
    """
    if request.user.is_superuser:
        cheese_categories = CheeseCategory.objects.all()
        beer_categories = BeerCategory.objects.all()
        template = 'products/edit-categories.html'
        context = {
            'cheese_categories': cheese_categories,
            'beer_categories': beer_categories
        }
        return render(request, template, context)
    else:
        return redirect('home')


def edit_cheese_category(request, category_id):
    """
    Allows user to edit individual cheese category
    """
    if request.method == 'POST':
        existing_category = get_object_or_404(CheeseCategory, pk=category_id)
        existing_name = existing_category.name
        # ensure there are no identically named (other) products
        category_test = CheeseCategory.objects.all()
        for test in category_test:
            if request.POST.get('name') == test.name:
                if test.name == existing_name:
                    continue
                else:
                    messages.error(
                        request, "There is already another " +
                        "category with this name, please try again")
                    return redirect(reverse(
                        'edit_cheese_category', args=[category_id]))
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
                image_alt = str(
                    "An image of " + request.POST.get('name') + " cheese")
                converted_image = imageConvert(
                    ImageUpload, 400, 75, "webp")
                if category.image_url != "":
                    cloudinary.uploader.destroy(
                        "cheese-and-beer/products/" + category.image_url)
                cloudinary.uploader.upload(
                    converted_image,
                    public_id=image_url,
                    folder="cheese-and-beer/products")
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
                updated_pairings = [int(x) for x in updated_pairings]
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
                    beer_to_add = get_object_or_404(
                        BeerCategory, pk=add_pairing)
                    category.pairs_with.add(beer_to_add)
            if pairings_to_remove:
                for remove_pairing in pairings_to_remove:
                    beer_to_remove = get_object_or_404(
                        BeerCategory, pk=remove_pairing)
                    category.pairs_with.remove(beer_to_remove)
            messages.success(request, 'Cheese category updated')
        else:
            messages.error(request, 'Failed to update category information')
    # returns updated data
    if request.user.is_superuser:
        category = get_object_or_404(CheeseCategory, pk=category_id)
        pairings = category.pairs_with.all()
        initial_pairings = pairings.values_list('id', flat=True)
        beer_categories = BeerCategory.objects.all()
        form = CheeseCategoryForm(instance=category)
        template = 'products/edit-cheese-category.html'
        context = {
            'initial_pairings': list(initial_pairings),
            'form': form,
            'category': category,
            'beer_categories': beer_categories
        }
        return render(request, template, context)
    else:
        return redirect('home')


def edit_beer_category(request, category_id):
    """
    Allows user to edit individual beer category
    """
    if request.method == 'POST':
        existing_category = get_object_or_404(BeerCategory, pk=category_id)
        existing_name = existing_category.name
        category_test = BeerCategory.objects.all()
        # ensure there are no identically named (other) products
        for test in category_test:
            if request.POST.get('name') == test.name:
                if test.name == existing_name:
                    continue
                else:
                    messages.error(
                        request, "There is already another " +
                        "category with this name, please try again")
                    return redirect(reverse(
                        'edit_beer_category', args=[category_id]))
        form = BeerCategoryForm(request.POST)
        if form.is_valid():
            category = get_object_or_404(BeerCategory, pk=category_id)
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
                image_alt = str(
                    "An image depicting some " + request.POST.get('name'))
                converted_image = imageConvert(
                    ImageUpload, 400, 75, "webp")
                if category.image_url != "":
                    cloudinary.uploader.destroy(
                        "cheese-and-beer/products/" + category.image_url)
                cloudinary.uploader.upload(
                    converted_image,
                    public_id=image_url,
                    folder="cheese-and-beer/products")
            else:
                image_url = category.image_url
                image_alt = category.image_alt
            BeerCategory.objects.filter(pk=category_id).update(
                name=request.POST.get('name'),
                description=request.POST.get('description'),
                image_url=image_url,
                image_alt=image_alt
            )
            # updates many to many pairings based on category buttons selected
            pairings = category.cheese.all()
            initial_pairings = list(pairings.values_list('id', flat=True))
            pairings_to_add = []
            pairings_to_remove = []
            if request.POST.get('pairings'):
                pairings_list = request.POST.get('pairings')[:-1]
                updated_pairings = list(pairings_list.split(','))
                updated_pairings = [int(x) for x in updated_pairings]
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
                    cheese_to_add = get_object_or_404(
                        CheeseCategory, pk=add_pairing)
                    category.cheese.add(cheese_to_add)
            if pairings_to_remove:
                for remove_pairing in pairings_to_remove:
                    cheese_to_remove = get_object_or_404(
                        CheeseCategory, pk=remove_pairing)
                    category.cheese.remove(cheese_to_remove)
            messages.success(request, 'Beer category updated')
        else:
            messages.error(request, 'Failed to update beer category')
    if request.user.is_superuser:
        category = get_object_or_404(BeerCategory, pk=category_id)
        pairings = category.cheese.all()
        initial_pairings = pairings.values_list('id', flat=True)
        cheese_categories = CheeseCategory.objects.all()
        form = BeerCategoryForm(instance=category)
        template = 'products/edit-beer-category.html'
        context = {
            'initial_pairings': list(initial_pairings),
            'form': form,
            'category': category,
            'cheese_categories': cheese_categories,
        }
        return render(request, template, context)
    else:
        return redirect('home')


def add_cheese(request):
    if request.user.is_superuser:
        """
        view renders the correct form to add a cheese
        """
        form = CheeseForm()
        template = 'products/add-cheese.html'
        context = {
            'form': form,
        }
        return render(request, template, context)
    else:
        return redirect('home')


def add_beer(request):
    """
    view renders the correct form to add a beer
    """
    if request.user.is_superuser:
        form = BeerForm()
        template = 'products/add-beer.html'
        context = {
            'form': form,
        }
        return render(request, template, context)
    else:
        return redirect('home')


def add_product(request):
    """
    this view processes a submitted beer or cheese form.
    """
    if request.user.is_superuser:
        product_type = request.POST.get('product_type')
        # ensure there are no identically named products
        products_test = Product.objects.all()
        for test in products_test:
            if request.POST.get('name') == test.name:
                messages.error(
                    request, "This product already exists, please try again")
                if product_type == "cheese":
                    return redirect('add_cheese')
                else:
                    return redirect('add_beer')
        # validate custom fields for type of product
        if product_type == "cheese":
            form = CheeseForm(request.POST)
            selected_category = form['cheese_category'].value()
            product_code = "PCH"
            if selected_category == "":
                messages.error(
                    request, 'Failed to add cheese, please select a category')
                return redirect('add_cheese')
            cheese_category = selected_category
        else:
            form = BeerForm(request.POST)
            selected_category = form['beer_category'].value()
            product_code = "PBE"
            if selected_category == "":
                messages.error(
                    request, 'Failed to add beer, please select a category')
                return redirect('add_beer')
            if form['container'].value() == "":
                messages.error(
                    request, 'Failed to add beer, ' +
                    'please select the container your beer is sold in')
                return redirect('add_beer')
            if form['alcohol_content'].value() == "":
                messages.error(request, 'Failed to add beer, please reveal ' +
                               'the alcohol content of the beer')
                return redirect('add_beer')
            beer_category = selected_category
        if form.is_valid():
            name = request.POST.get('name').lower()
            ImageUpload = request.FILES.get('image')
            # reverts image to generic category image if none added
            # reverts description to category description if none added
            if request.POST.get('description'):
                description = request.POST.get('description')
            else:
                if product_type == "cheese":
                    category = get_object_or_404(
                        CheeseCategory, pk=cheese_category)
                else:
                    category = get_object_or_404(
                        BeerCategory, pk=beer_category)
                description = category.description
            # adds a price per kilo or price per litre
            amount = decimal.Decimal(form['amount'].value())
            price = decimal.Decimal(request.POST.get('price'))
            new_price = (1000/amount)*price
            price_per_amount = new_price.quantize(decimal.Decimal('0.00'))
            image_id = str(datetime.now().timestamp()).split('.')[1]
            product_number = product_code + uuid.uuid4().hex.upper()
            if ImageUpload:
                image_url = str(
                    re.sub(
                        "[.!# $%;@&'*+/=?^_` {|}~]",
                        "-",
                        name
                        ) + "-" + image_id
                    )
                image_alt = str("An image depicting " + form['name'].value())
                converted_image = imageConvert(
                    ImageUpload, 400, 75, "webp")
                cloudinary.uploader.upload(
                    converted_image,
                    public_id=image_url,
                    folder="cheese-and-beer/products")
            else:
                # reverts image to generic category image if none added
                if product_type == "cheese":
                    category = get_object_or_404(
                        CheeseCategory, pk=cheese_category)
                else:
                    category = get_object_or_404(
                        BeerCategory, pk=beer_category)
                image_url = category.image_url
                image_alt = category.image_alt
            final_form = form.save(commit=False)
            final_form.product_number = product_number
            final_form.product_type = product_type
            final_form.description = description
            final_form.image_url = image_url
            final_form.image_alt = image_alt
            final_form.price_per_amount = price_per_amount
            final_form.save()
            if product_type == "cheese":
                messages.success(request, 'New Cheese Added')
                return redirect('admin_console')
            else:
                messages.success(request, 'New Beer Added')
                return redirect('admin_console')
        else:
            if product_type == "cheese":
                messages.error(
                    request, 'Failed to add cheese, please ensure all ' +
                    'fields are filled out correctly')
                return redirect('add_cheese')
            else:
                messages.error(
                    request, 'Failed to add beer, please ensure all ' +
                    'fields are filled out correctly')
                return redirect('add_beer')
    else:
        return redirect('home')


def edit_product(request):
    """
    This view enables and admin user to view a list of products to edit
    or perform a basic search.
    """
    if request.user.is_superuser:
        products = Product.objects.all()
        query = None
        if request.GET:
            if 'q' in request.GET:
                query = request.GET['q'].strip()
                if not query:
                    return redirect('edit_product')
            queries = Q(
                product_number__iexact=query) | Q(name__icontains=query)
            products = products.filter(queries)
        template = 'products/edit-product.html'
        context = {
            'search_term': query,
            'products': products,
        }
        return render(request, template, context)
    else:
        return redirect('home')


def product_edit(request, product_id):
    """
    This view enables renders a populated form to edit a product (depending
    on product type) and processes submitted forms.
    """
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        existing_name = product.name
        # ensure there are no identically named (other) products
        products_test = Product.objects.all()
        for test in products_test:
            if request.POST.get('name') == test.name:
                if test.name == existing_name:
                    continue
                else:
                    messages.error(
                        request, "There is already another product " +
                        "with this name, please try again")
                    return redirect(reverse('product_edit', args=[product_id]))
        if product.product_type == "cheese":
            form = CheeseForm(request.POST, instance=product)
            selected_category = form['cheese_category'].value()
            if selected_category == "":
                messages.error(
                    request, 'Failed to edit cheese, please select a category')
                return redirect(reverse('product_edit', args=[product_id]))
            if form['texture'].value() == "":
                messages.error(
                    request, 'Failed to edit product, please add texture')
                return redirect(reverse('product_edit', args=[product_id]))
            cheese_category = selected_category
        else:
            form = BeerForm(request.POST, instance=product)
            selected_category = form['beer_category'].value()
            if selected_category == "":
                messages.error(
                    request, 'Failed to add beer, please select a category')
                return redirect(reverse('product_edit', args=[product_id]))
            if form['container'].value() == "":
                messages.error(
                    request, 'Failed to add beer, please select what ' +
                    'your beer is sold in')
                return redirect(reverse('product_edit', args=[product_id]))
            if form['alcohol_content'].value() == "":
                messages.error(request, 'Failed to add beer, please reveal ' +
                               'the alcohol content of the beer')
                return redirect(reverse('product_edit', args=[product_id]))
            beer_category = selected_category
        if form['variety'].value() == "":
            messages.error(
                request, 'Failed to edit product, please select variety')
            return redirect(reverse('product_edit', args=[product_id]))
        if form.is_valid():
            name = request.POST.get('name').lower()
            ImageUpload = request.FILES.get('image')
            # reverts description to category description if none added
            if request.POST.get('description'):
                description = request.POST.get('description')
            else:
                if product.product_type == "cheese":
                    category = get_object_or_404(
                        CheeseCategory, pk=cheese_category)
                else:
                    category = get_object_or_404(
                        BeerCategory, pk=beer_category)
                description = category.description
                print(description)
            # adds a price per kilo or price per litre
            amount = decimal.Decimal(form['amount'].value())
            price = decimal.Decimal(request.POST.get('price'))
            new_price = (1000/amount)*price
            price_per_amount = new_price.quantize(decimal.Decimal('0.00'))
            image_id = str(datetime.now().timestamp()).split('.')[1]
            if ImageUpload:
                image_url = str(
                    re.sub(
                        "[.!# $%;@&'*+/=?^_` {|}~]",
                        "-",
                        name
                        ) + "-" + image_id
                    )
                image_alt = str("An image depicting " + form['name'].value())
                converted_image = imageConvert(
                    ImageUpload, 400, 75, "webp")
                if product.image_url:
                    cloudinary.uploader.destroy(
                        "cheese-and-beer/products/" + product.image_url)
                cloudinary.uploader.upload(
                    converted_image,
                    public_id=image_url,
                    folder="cheese-and-beer/products")
            else:
                image_url = product.image_url
                image_alt = product.image_alt
            final_form = form.save(commit=False)
            final_form.product_type = product.product_type
            final_form.description = description
            final_form.image_url = image_url
            final_form.image_alt = image_alt
            final_form.price_per_amount = price_per_amount
            final_form.save()
            if product.product_type == "cheese":
                messages.success(request, 'Cheese Updated')
            else:
                messages.success(request, 'Beer Updated')
        else:
            if product.product_type == "cheese":
                messages.error(
                    request, 'Failed to edit cheese, please ensure all ' +
                    'fields are filled out correctly')
            else:
                messages.error(
                    request, 'Failed to edit beer, please ensure all fields ' +
                    'are filled out correctly')
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=product_id)
        if product.product_type == "cheese":
            form = CheeseForm(instance=product)
        else:
            form = BeerForm(instance=product)
        template = 'products/product-edit.html'
        context = {
            'product': product,
            'form': form,
        }
        return render(request, template, context)
    else:
        return redirect('home')


def product_publish(request, product_id):
    """
    This function processes the toggle function in the edit product
    view. if a product is unpublished it is not visible in searches and
    cannot be purchased.  If a product has sold items in the past it cannot
    be deleted; this is a preferable way of preventing further sales whilst
    preserving sales and order data, and is prevalent with major online stores.
    """
    if request.user.is_superuser:
        Product.objects.filter(pk=product_id).update(
                displayed=True
            )
        return redirect(reverse('product_edit', args=[product_id]))
    else:
        return redirect('home')


def product_unpublish(request, product_id):
    """
    This function processes the toggle function in the edit product
    view.
    """
    if request.user.is_superuser:
        Product.objects.filter(pk=product_id).update(
                displayed=False
            )
        return redirect(reverse('product_edit', args=[product_id]))
    else:
        return redirect('home')


def delete_product(request, product_id):
    """
    This function enables a superuser to delete a product which has yet to
    sell any units (perhaps one created by accident or as a test)
    """
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=product_id)
        if product.image_url != "":
            cloudinary.uploader.destroy(
                "cheese-and-beer/products/" + product.image_url)
        product.delete()
        messages.success(request, 'Product Deleted')
        return redirect('edit_product')
    else:
        return redirect('home')
