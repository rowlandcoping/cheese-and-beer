from django import forms
from .models import cheese_category, beer_category


class CheeseCategoryForm(forms.ModelForm):

    class Meta:
        model = cheese_category
        fields = '__all__'


    # this overrides .init to customise fields.  may not be needed yet
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)