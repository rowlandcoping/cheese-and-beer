from django.shortcuts import render
from products.models import CheeseCategory, BeerCategory

# Create your views here.

def index(request):
    """ Returns home page"""
    beer_categories=BeerCategory.objects.all()
    cheese_categories=CheeseCategory.objects.all()
    superuser = request.user.is_superuser
    authenticated = request.user.is_authenticated
    context={
        'authenticated': authenticated,
        'superuser': superuser,
        'beer_categories': beer_categories,
        'cheese_categories': cheese_categories
    }
    return render(request, 'home/index.html', context)
