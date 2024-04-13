from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from checkout .models import Order, OrderItems
from addresses .models import Addresses

from django.views.decorators.http import require_POST


def account_overview(request):
    addresses= Addresses.objects.filter(user_id=request.user.id)
    orders = Order.objects.filter(user_id=request.user)
    template = 'user_account/my-account.html'    
    context = {
        'addresses': addresses,
        'orders': orders
    }
    return render(request, template, context)


def view_orders(request):
    orders = Order.objects.filter(user_id=request.user).order_by('-order_date')
    template = 'user_account/orders.html'    
    context = {
        'orders': orders
    }
    return render(request, template, context)


def order_info(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    items = OrderItems.objects.filter(order_id=order).order_by('-id')
    template = 'user_account/order-info.html'    
    context = {
        'order': order,
        'items': items
    }
    return render(request, template, context)