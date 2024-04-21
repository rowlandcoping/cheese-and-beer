from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from addresses.models import Addresses
from .models import Order, OrderItems
from products.models import Product
from django.db.models import Sum

import json
import time
import stripe


class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    
    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/header.txt',
            {'order': order})
        message = render_to_string(
            'checkout/confirmation_emails/body.txt',
            {'order': order })        
        send_mail(
            subject,
            message, 
            settings.DEFAULT_FROM_EMAIL,                       
            [cust_email]
        )

   
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook happened: {event["type"]}',
            status=200)
    

    def handle_payment_intent_succeeded(self, event):
        
        #retrieve pid from intent to check if order exists
        intent=event.data.object
        pid=intent.id
        
        #test if order exists, using pid
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(stripe_pid=pid)
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            user_id = None
            address = None
            basket=intent.metadata.basket
            stripe_charge = stripe.Charge.retrieve(
                intent.latest_charge
            )            
            email = stripe_charge.billing_details.email
            shipping_details = intent.shipping
            # check if user exists, assign order to them if they do
            user_check = User.objects.all()
            for check in user_check:
                if check.email == email:
                    user_id = check
                    print(user_id)
                    print(user_id.id)
                    # then check if the address matches any of their saved ones
                    address_check = Addresses.objects.all()
                    for check in address_check:
                        print(check.user_id.id)
                        if user_id.id == check.user_id.id:
                            if shipping_details.address.postal_code == check.postcode and shipping_details.name == check.full_name and shipping_details.address.line1 == check.address_line_one:
                                address = check
                                break
                    break
            for field, value in shipping_details.address.items():
                if value == "":
                    shipping_details.address[field] = None
            items_total=intent.metadata.items_total
            delivery_cost = intent.metadata.delivery_cost           
            time_created = datetime.now()
            delivery_date = datetime.now() + timedelta(days=5)
            grand_total = round(stripe_charge.amount / 100, 2)
            try:
                order = Order.objects.create(
                    user_id = user_id,
                    shipping_id = address,
                    email = email,
                    full_name = shipping_details.name,
                    address_line_one = shipping_details.address.line1,
                    address_line_two = shipping_details.address.line2,
                    town_or_city = shipping_details.address.city,
                    county = shipping_details.address.state,
                    postcode = shipping_details.address.postal_code,
                    order_date = time_created,
                    delivery_date = delivery_date,
                    items_total = items_total,
                    delivery_cost = delivery_cost,
                    grand_total = grand_total,
                    stripe_pid = pid,
                )
                for item_id, item_data in json.loads(basket).items():                    
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItems(
                            order_id=order,
                            product_type = product.product_type,
                            product=product,
                            price=product.price,
                            quantity=item_data,
                        )
                    order_item.save()
                    units_sold = OrderItems.objects.filter(product=product).aggregate(Sum('quantity'))
                    Product.objects.filter(pk=product.id).update(
                        units_sold = units_sold['quantity__sum']
                    )          
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)        
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)
    

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook failure notification received:{event["type"]}',
            status=200
        )