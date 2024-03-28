from django import forms
from .models import Addresses


class AddressForm(forms.ModelForm):

    class Meta:
        model = Addresses
        fields = (
            'full_name',
            'address_line_one',
            'address_line_two',
            'town_or_city',
            'county',
            'postcode',        
        )