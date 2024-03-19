from django.contrib import admin
from .models import BeerCategory, CheeseCategory, Product


admin.site.register(BeerCategory)
admin.site.register(CheeseCategory)
admin.site.register(Product)