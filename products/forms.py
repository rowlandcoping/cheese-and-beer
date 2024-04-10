from django import forms
from .models import CheeseCategory, BeerCategory, Product


class BeerCategoryForm(forms.ModelForm):

    class Meta:
        model = BeerCategory
        fields = ('name', 'description',)
        
    image = forms.ImageField(label='Image', required=False)
    

class CheeseCategoryForm(forms.ModelForm):

    class Meta:
        model = CheeseCategory
        fields = ('name', 'description')
    
    image = forms.ImageField(label='Image', required=False)


class BeerForm(forms.ModelForm):
    quantity_options = (
        ('175', '175ml'),
        ('250', '250ml'),
        ('330', '330ml'),
        ('400', '400ml'),
        ('500', '500ml')
    )
    type_options = (
        ('bottle', 'bottle'),
        ('can', 'can'), 
    )
    container = forms.ChoiceField(label='Comes In', widget=forms.RadioSelect, choices=type_options)
    amount = forms.ChoiceField(label='Amount', widget=forms.Select, choices=quantity_options)
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Product
        fields = (
            'name',
            'beer_category',
            'description',
            'variety',
            'alcohol_content',
            'container',
            'amount',           
            'price',            
            'country_origin',
            'image',
        )
    

class CheeseForm(forms.ModelForm):
    quantity_options = (
        ('100', '100g'),
        ('125', '125g'),
        ('150', '150g'),
        ('175', '175g'),
        ('200', '200g'),
        ('250', '250g'),
        ('350', '350g'),
        ('500', '500g'),
    )
    amount = forms.ChoiceField(label='Amount', widget=forms.Select, choices=quantity_options)
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Product
        fields = (
            'name',
            'cheese_category',
            'description',
            'variety',
            'texture',
            'amount',
            'price',
            'country_origin',
            'image',
        )
