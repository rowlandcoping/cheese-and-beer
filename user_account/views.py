from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from checkout .models import Order, OrderItems
from addresses .models import Addresses
from django.db.models import Q

from django.views.decorators.http import require_POST


def account_overview(request):
    if request.user.is_authenticated:
        addresses= Addresses.objects.filter(user_id=request.user.id)
        orders = Order.objects.filter(user_id=request.user)
        template = 'user_account/my-account.html'    
        context = {
            'addresses': addresses,
            'orders': orders
        }
        return render(request, template, context)
    return redirect('account_login')


def view_orders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user_id=request.user).order_by('-order_date')
        query = None
        if request.GET:
            if 'q' in request.GET:
                query = request.GET['q'].strip()            
                if not query:
                    messages.error(request, 'Please enter something to search for')
                    return redirect('view_orders')
            queries = Q(order_number__iexact=query) | Q(postcode__iexact=query)
            orders = orders.filter(queries)
        template = 'user_account/orders.html'    
        context = {
            'orders': orders
        }
        return render(request, template, context)
    return redirect('account_login')


def order_info(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    items = OrderItems.objects.filter(order_id=order).order_by('-id')
    template = 'user_account/order-info.html'    
    context = {
        'order': order,
        'items': items
    }
    return render(request, template, context)


def found_order(request):
    if request.method == 'POST':
        order_number = request.POST.get('order-number')
        email = request.POST.get('email')
        postcode = request.POST.get('postcode')
        order = Order.objects.get(order_number = order_number, email = email, postcode = postcode)
        if order:
            items = OrderItems.objects.filter(order_id__id=order.id)
        else:
            messages.error((request, 'Order not found'))
            return redirect('find_order')
    template = 'user_account/order-info.html'    
    context = {
        'order': order,
        'items': items
    }
    return render(request, template, context)


def find_order(request):
    template = 'user_account/find-order.html'
    return render(request, template)
