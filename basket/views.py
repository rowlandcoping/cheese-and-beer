from django.shortcuts import redirect, render
from products.models import Product
from basket.contexts import basket_total
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.conf import settings

url = settings.MEDIA_URL
def make_safe(message):
    return mark_safe(message)


def buy_now(request):
    if 'single' in request.GET:
        product = int(request.GET['single'].split(',')[0])
        quantity = int(request.GET['single'].split(',')[1])
        basket = request.session.get('basket', {})
        basket[product] = quantity
        request.session['basket'] = basket
    elif 'remove' in request.GET:        
        product = int(request.GET['remove'].split(',')[0])
        quantity = int(request.GET['remove'].split(',')[1])
        del request.session['basket']
        basket = request.session.get('basket', {})
        basket[product] = quantity
        request.session['basket'] = basket
    else:
        product = request.GET['addon'].split(',')[0]
        quantity = int(request.GET['addon'].split(',')[1])
        basket = request.session.get('basket', {})
        if product in list(basket.keys()):
            basket[product] += quantity
        else:
            basket[product] = quantity
        request.session['basket'] = basket
    product_info = Product.objects.get(pk=product)
    message = '<p>' + product_info.name + ' added to basket</p>' + '<img src="' + url.strip() + f'products/{ product_info.image_url }">'                         
    messages.success(request, make_safe(message))
    return redirect('checkout')    


def add_to_basket(request):
    quantity = int(request.POST.get('quantity'))
    view = request.POST.get('view')
    product = request.POST.get('product')
    product_info = Product.objects.get(pk=product)
    basket = request.session.get('basket', {})
    if product in list(basket.keys()):
        basket[product] += quantity
    else:
        basket[product] = quantity
    request.session['basket'] = basket
    message = '<p>' + product_info.name + ' added to basket</p>' + '<img src="' + url.strip() + f'products/{ product_info.image_url }">'                         
    messages.success(request, make_safe(message))
    return redirect(view)

def update_basket(request):
    action = request.GET['action'].split(',')[0]
    product_id = request.GET['action'].split(',')[1]
    product_info = Product.objects.get(pk=product_id)
    origin = request.GET['action'].split(',')[2]
    basket = request.session.get('basket', {})
    if action == "increment":
        basket[product_id] += 1
        message = '<p>' + product_info.name + ' added to basket</p>' + '<img src="' + url.strip() + f'products/{ product_info.image_url }">' 
        messages.success(request, make_safe(message))
    else:
        if basket[product_id] > 1:
            basket[product_id] -= 1
        message = '<p>' + product_info.name + ' removed from basket</p>' + '<img src="' + url.strip() + f'products/{ product_info.image_url }">' 
        messages.warning(request, make_safe(message))
    request.session['basket'] = basket
    if origin == "chkt":
        return redirect('checkout')
    else:
        return redirect('view_basket')
    
def remove_item(request):
    product_id = request.GET['remove']
    product_info = Product.objects.get(pk=product_id)   
    basket = request.session.get('basket', {})
    if basket[product_id]:
        basket.pop(product_id)
    if basket:
        request.session['basket'] = basket
        message = '<p>' + product_info.name + ' removed from basket</p>' + '<img src="' + url.strip() + f'products/{ product_info.image_url }">' 
        messages.warning(request, make_safe(message))
    else:
        if 'basket' in request.session:
            del request.session['basket']
        if 'intent_id' in request.session:
            del request.session['intent_id']
        if 'selected_address' in request.session:
            del request.session['selected_address']
        messages.warning(request, (
                        "You have removed everything from your basket.")
                    )
        return redirect('home')
    return redirect('view_basket')


def view_basket(request):
    basket = request.session.get('basket', {})
    if not basket:
        return redirect('home')
    current_basket = basket_total(request)

    template = 'basket/basket.html'
    context = {
        'products': current_basket,
    }
    return render(request, template, context)