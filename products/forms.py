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

    class Meta:
        model = Product
        fields = (
            'name',
            'beer_category',
            'description',
            'variety',
            'alcohol_content',
            'country_origin'
        )
        
    image = forms.ImageField(label='Image', required=False)
    

class CheeseForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'name',
            'cheese_category',
            'description',
            'variety',
            'country_origin'
        )
    
    image = forms.ImageField(label='Image', required=False)
    

    # this overrides .init to customise fields.  may not be needed yet
    # def __init__(self, *args, **kwargs):
    #   super().__init__(*args, **kwargs)
