from django.shortcuts import render
from .models import cheese_category
from .forms import CheeseCategoryForm

# Create your views here.

def add_cheese_category(request):
    """ Returns form to add a cheese category"""

    form = CheeseCategoryForm()
        
    template = 'products/add-cheese-category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)