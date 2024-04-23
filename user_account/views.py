from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from checkout.models import Order, OrderItems
from products.models import Product
from addresses.models import Addresses
from .forms import ContactForm
from django.db.models import Q
from .models import Wishlist
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


url = settings.MEDIA_URL


def make_safe(message):
    return mark_safe(message)


def account_overview(request):
    """
    Displays user's account overview page with access to various site features.
    """
    if request.user.is_authenticated:
        addresses = Addresses.objects.filter(user_id=request.user.id)
        orders = Order.objects.filter(user_id=request.user)
        template = 'user_account/my-account.html'
        context = {
            'addresses': addresses,
            'orders': orders
        }
        return render(request, template, context)
    return redirect('account_login')


def view_orders(request):
    """
    Allows users to view a summary of previous orders or search for specific
    order.  Provides access to more detailed view, or a pre-populated contact
    page.
    """
    if request.user.is_authenticated:
        orders = Order.objects.filter(
            user_id=request.user).order_by('-order_date')
        query = None
        if request.GET:
            if 'q' in request.GET:
                query = request.GET['q'].strip()
                if not query:
                    messages.error(
                        request, 'Please enter something to search for')
                    return redirect('view_orders')
            queries = Q(order_number__iexact=query) | Q(postcode__iexact=query)
            orders = orders.filter(queries)
        template = 'user_account/orders.html'
        context = {
            'query': query,
            'orders': orders
        }
        return render(request, template, context)
    return redirect('account_login')


def order_info(request, order_id):
    """
    Provides a product list for a selected previous order. Can be accessed
    by users who are not signed in via the find orders view or the order
    confirmation page.
    """
    order = get_object_or_404(Order, pk=order_id)
    items = OrderItems.objects.filter(order_id=order).order_by('-id')
    template = 'user_account/order-info.html'
    context = {
        'order': order,
        'items': items
    }
    return render(request, template, context)


def found_order(request):
    """
    Takes specific details to allow unregistered users to access their past
    orders, returns them to the order_info view.
    """
    if request.method == 'POST':
        order_number = request.POST.get('order-number')
        email = request.POST.get('email')
        postcode = request.POST.get('postcode')
        order = Order.objects.get(
            order_number=order_number, email=email, postcode=postcode)
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
    """
    View returns a form which unregistered users can use to find their
    past orders.
    """
    template = 'user_account/find-order.html'
    return render(request, template)


def wishlist(request):
    """
    Returns a view with a list of items on the user's wishlist.
    """
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user.id)
        template = 'user_account/wishlist.html'
        context = {
            'wishlist': wishlist,
        }
        return render(request, template, context)
    else:
        messages.error(
            request, "You need to be logged in to view your wishlist")
        return redirect('home')


def add_to_wishlist(request):
    """
    Adds an item to the wishlist model with user and product foreign keys.
    returns user to the view they were previously on.
    """
    if request.method == 'POST':
        view = request.POST.get('view')
        product_id = request.POST.get('product')
        product = Product.objects.get(pk=product_id)
        user = request.user
        Wishlist.objects.create(
                    user=user,
                    product=product,
                )
        message = (
            '<p>' + product.name + ' added to wishlist</p>' + '<img src="' +
            url.strip() + f'products/{ product.image_url }">')
        messages.success(request, make_safe(message))
        return redirect(view)
    else:
        return redirect('home')


def remove_from_wishlist(request):
    """
    Removes an item to the wishlist model.
    returns user to the view they were previously on.
    """
    if request.method == 'POST':
        view = request.POST.get('view')
        product_id = request.POST.get('product')
        product = Product.objects.get(pk=product_id)
        item = Wishlist.objects.get(user=request.user, product=product)
        item.delete()
        message = ('<p>' + product.name + ' removed from wishlist</p>' +
                   '<img src="' + url.strip() +
                   f'products/{ product.image_url }">')
        messages.error(request, make_safe(message))
        return redirect(view)
    else:
        return redirect('home')


def contact_form(request):
    """
    This view returns a contact form, prepopulated with order details if the
    user clicked through from a particular order, and with user e-mail if they
    are logged in. Also processes messages, and provides e-mail confimation.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            order_number = request.POST.get('order_number')
            if order_number:
                order = Order.objects.get(order_number=order_number)
            else:
                order = None
            email = request.POST.get('email')
            message = request.POST.get('message')
            final_form = form.save(commit=False)
            final_form.user = user
            final_form.order = order
            final_form.save()
            cust_email = email
            subject = render_to_string(
                'user_account/confirmation_emails/header.txt',
                {})
            message = render_to_string(
                'user_account/confirmation_emails/body.txt',
                {'order_number': order_number, 'message': message})
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )
            return redirect(reverse('message_sent', args=[email]))
    if request.GET:
        if 'order_number' in request.GET:
            order_number = request.GET['order_number']
    else:
        order_number = ""
    if request.user.is_authenticated:
        user_email = request.user.email
    else:
        user_email = ""
    form = ContactForm()
    template = 'user_account/contact.html'
    context = {
        'order_number': order_number,
        'form': form,
        'email': user_email
    }
    return render(request, template, context)


def message_sent(request, email):
    """
    A confirmation page for when a user has sent a message successfully
    """
    template = 'user_account/message-sent.html'
    context = {
        'email': email,
    }
    return render(request, template, context)
