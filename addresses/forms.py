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
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)        
        placeholders = {
            'full_name': 'Full Name',
            'address_line_one': 'Address 1',
            'address_line_two': 'Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postcode',      
        }
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs.update({'style': 'font-family: "Times New Roman"; font-size:95%;'})