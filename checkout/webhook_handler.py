from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order
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
        print("HELP ME MOMMY")
        intent=event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook successfully received:{event["type"]}',
            status=200
        )
    

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received:{event["type"]}',
            status=200
        )