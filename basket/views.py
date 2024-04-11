from django.shortcuts import redirect, render
import stripe
from django.conf import settings
from basket.contexts import basket_total
import json

# Create your views here.

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
    return redirect('checkout')    


def add_to_basket(request):    
    quantity = int(request.POST.get('quantity'))
    view = request.POST.get('view')
    product = request.POST.get('product')
    basket = request.session.get('basket', {})
    if product in list(basket.keys()):
        basket[product] += quantity
    else:
        basket[product] = quantity
    request.session['basket'] = basket
    return redirect(view)

def update_basket(request):
    action = request.GET['action'].split(',')[0]
    product_id = request.GET['action'].split(',')[1]
    origin = request.GET['action'].split(',')[2]
    basket = request.session.get('basket', {})
    if action == "increment":
        basket[product_id] += 1
    else:
        if basket[product_id] > 1:
            basket[product_id] -= 1
    request.session['basket'] = basket
    if origin == "chkt":
        return redirect('checkout')
    else:
        return redirect('view_basket')
    
def remove_item(request):
    product_id = request.GET['remove']    
    basket = request.session.get('basket', {})
    if basket[product_id]:
        basket.pop(product_id)
    print(basket)
    if basket:
        request.session['basket'] = basket
    else:
        if 'basket' in request.session:
            del request.session['basket']
        if 'intent_id' in request.session:
            del request.session['intent_id']
        if 'selected_address' in request.session:
            del request.session['selected_address']
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