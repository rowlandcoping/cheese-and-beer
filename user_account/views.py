from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from checkout .models import Order, OrderItems

from django.views.decorators.http import require_POST


def account_overview(request):
    template = 'user_account/my-account.html'    
    context = {
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