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
        ('1', '175ml'),
        ('2', '250ml'),
        ('2', '330ml'),
        ('3', '400ml'),
        ('4', '500ml')
    )
    quantity = forms.ChoiceField(label='Quantity', widget=forms.Select, choices=quantity_options)
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Product
        fields = (
            'name',
            'beer_category',
            'description',
            'variety',
            'alcohol_content',
            'quantity',            
            'price',            
            'country_origin',
            'image',
        )
    

class CheeseForm(forms.ModelForm):
    quantity_options = (
        ('1', '100g'),
        ('2', '125g'),
        ('3', '150g'),
        ('4', '175g'),
        ('5', '200g'),
        ('6', '250g'),
        ('7', '350g'),
        ('8', '500g'),
    )
    quantity = forms.ChoiceField(label='Quantity', widget=forms.Select, choices=quantity_options)
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = Product
        fields = (
            'name',
            'cheese_category',
            'description',
            'variety',
            'quantity',
            'price',
            'country_origin',
            'image',
        )

    # this overrides .init to customise fields.  may not be needed yet
    # def __init__(self, *args, **kwargs):
    #   super().__init__(*args, **kwargs)
