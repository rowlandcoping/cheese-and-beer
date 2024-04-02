from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'user_id',
            'shipping_id',
            'email',
            'full_name',
            'address_line_one',
            'address_line_two',
            'town_or_city',
            'county',
            'postcode',
            'order_date',
            'delivery_date',
            'items_total',
            'delivery_cost',
            'grand_total',
            'stripe_pid',       
        )