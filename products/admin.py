from django.contrib import admin
from .models import BeerCategory, CheeseCategory


admin.site.register(BeerCategory)
admin.site.register(CheeseCategory)