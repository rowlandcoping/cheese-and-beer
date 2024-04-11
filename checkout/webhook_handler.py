from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime, timedelta

from .models import Order, OrderItems
from products.models import Product

import json
import time
import stripe


class StripeWH_Handler:
    def __init__(self, request):
        self.request = request
    
    
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
            basket=intent.metadata.basket
            stripe_charge = stripe.Charge.retrieve(
                intent.latest_charge
            )
            user_id = intent.metadata.username
            email = stripe_charge.billing_details.email
            shipping_details = intent.shipping
            for field, value in shipping_details.address.items():
                if value == "":
                    shipping_details.address[field] = None
            time_created = datetime.now()
            delivery_date = datetime.now() + timedelta(days=5)
            try:
                order = Order.objects.create(
                    user_id = user_id,
                    shipping_id = intent.metadata.address_id,
                    email = email,
                    full_name = shipping_details,
                    address_line_one = shipping_details.line1,
                    address_line_two = shipping_details.line2,
                    town_or_city = shipping_details.city,
                    county = shipping_details.state,
                    postcode = shipping_details.postal_code,
                    order_date = time_created,
                    delivery_date = delivery_date,
                    items_total = json.loads(basket['basket_total']),
                    delivery_cost = json.loads(basket['delivery_charge']),
                    grand_total = round(stripe_charge.amount / 100, 2),
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
            content=f'Webhook received:{event["type"]}',
            status=200
        )