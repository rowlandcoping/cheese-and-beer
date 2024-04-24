from django.http import HttpResponse
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
        """
        Function to send the user a confirmation e-mail.
        I have adapted this code from the Boutique Ado tutorial site
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/header.txt',
            {'order': order})
        message = render_to_string(
            'checkout/confirmation_emails/body.txt',
            {'order': order})
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event.
        This function originates from the Boutique Ado tutorial site
        """
        return HttpResponse(
            content=f'Unhandled Webhook happened: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle a webhook indicating a payment has been processed.
        Some elements of this code are from the Boutique Ado tutorial site,
        however it has been heavily customised
        """
        # retrieve pid from intent to check if order exists
        intent = event.data.object
        pid = intent.id
        # test if order exists, using pid
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
                content="Webhook received: " + event["type"] +
                "| SUCCESS: Verified order already in database",
                status=200)
        else:
            order = None
            user_id = None
            address = None
            basket = intent.metadata.basket
            stripe_charge = stripe.Charge.retrieve(
                intent.latest_charge
            )
            email = stripe_charge.billing_details.email
            shipping_details = intent.shipping
            # check if user exists, assigns order to them if they do
            user_check = User.objects.all()
            for check in user_check:
                if check.email == email:
                    user_id = check
                    # then check if the address matches any of their saved ones
                    address_check = Addresses.objects.all()
                    for check in address_check:
                        if user_id.id == check.user_id.id:
                            ad = shipping_details.address.line1
                            po = shipping_details.address.postal_code.upper()
                            na = shipping_details.name
                            cpo = check.postcode
                            cna = check.full_name
                            cad = check.address_line_one
                            if po == cpo and na == cna and ad == cad:
                                address = check
                                break
                    break
            for field, value in shipping_details.address.items():
                if value == "":
                    shipping_details.address[field] = None
            items_total = intent.metadata.items_total
            delivery_cost = intent.metadata.delivery_cost
            time_created = datetime.now()
            delivery_date = datetime.now() + timedelta(days=5)
            grand_total = round(stripe_charge.amount / 100, 2)
            try:
                order = Order.objects.create(
                    user_id=user_id,
                    shipping_id=address,
                    email=email,
                    full_name=shipping_details.name,
                    address_line_one=shipping_details.address.line1,
                    address_line_two=shipping_details.address.line2,
                    town_or_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code.upper(),
                    order_date=time_created,
                    delivery_date=delivery_date,
                    items_total=items_total,
                    delivery_cost=delivery_cost,
                    grand_total=grand_total,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItems(
                            order_id=order,
                            product_type=product.product_type,
                            product=product,
                            price=product.price,
                            quantity=item_data,
                        )
                    order_item.save()
                    units_sold = OrderItems.objects.filter(
                        product=product).aggregate(Sum('quantity'))
                    Product.objects.filter(pk=product.id).update(
                        units_sold=units_sold['quantity__sum']
                    )
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
                content="Webhook received: " + event["type"] +
                "| SUCCESS: Verified order already in database",
                status=200)

    def handle_failure(self, event):
        """
        Handle a webhook indicating a payment has failed to be processed.
        This function originates from the Boutique Ado tutorial site
        """
        return HttpResponse(
            content=f'Webhook failure notification received:{event["type"]}',
            status=200
        )
