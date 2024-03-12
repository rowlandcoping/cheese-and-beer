from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add-cheese-catgory/', views.add_cheese_category, name='add_cheese_category'),
    path('add-beer-catgory/', views.add_beer_category, name='add_beer_category'),
]

