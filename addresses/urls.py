from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('manage-addresses/', views.manage_addresses, name='manage_addresses'),
    path('add-address/', views.add_address, name='add_address')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)