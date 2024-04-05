from django.shortcuts import redirect
import stripe
from django.conf import settings
from basket.contexts import basket_total
import json

# Create your views here.

def buy_now(request):
    if 'single' in request.GET:
        product = request.GET['single']
        basket = request.session.get('basket', {})
        basket[product] = 1
        request.session['basket'] = basket
    elif 'remove' in request.GET:        
        product = request.GET['remove']
        del request.session['basket']
        basket = request.session.get('basket', {})
        basket[product] = 1
        request.session['basket'] = basket
        intent_id = request.session.get('intent_id', {})
        if intent_id:
            stripe_secret_key = settings.STRIPE_SECRET_KEY
            stripe.api_key = stripe_secret_key
            intent_id = request.session.get('intent_id', {})
            pid = intent_id['secret'].split('_secret')[0]
            current_basket = basket_total(request)
            total = current_basket['grand_total']
            stripe_total = round(total * 100)
            stripe.PaymentIntent.modify(pid, amount=stripe_total, metadata={
                'basket': json.dumps(request.session.get('basket', {})),
                'username': request.user,
                })
    else:
        product = request.GET['addon']
        basket = request.session.get('basket', {})
        if product in list(basket.keys()):
            basket[product] += 1
        else:
            basket[product] = 1
        request.session['basket'] = basket
        intent_id = request.session.get('intent_id', {})
        if intent_id:
            stripe_secret_key = settings.STRIPE_SECRET_KEY
            stripe.api_key = stripe_secret_key
            intent_id = request.session.get('intent_id', {})
            pid = intent_id['secret'].split('_secret')[0]
            current_basket = basket_total(request)
            total = current_basket['grand_total']
            stripe_total = round(total * 100)
            stripe.PaymentIntent.modify(pid, amount=stripe_total, metadata={
                'basket': json.dumps(request.session.get('basket', {})),
                'username': request.user,
                })
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
    intent_id = request.session.get('intent_id', {})
    if intent_id:
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        stripe.api_key = stripe_secret_key
        intent_id = request.session.get('intent_id', {})
        pid = intent_id['secret'].split('_secret')[0]
        current_basket = basket_total(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.PaymentIntent.modify(pid, amount=stripe_total, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'username': request.user,
            })
    return redirect(view)