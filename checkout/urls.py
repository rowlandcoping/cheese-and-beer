from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('update_basket/', views.update_basket, name='update_basket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)