from django import forms
from .models import CheeseCategory, BeerCategory


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


    # this overrides .init to customise fields.  may not be needed yet
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)