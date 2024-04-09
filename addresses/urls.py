from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('addresses/', views.manage_addresses, name='manage_addresses'),
    path('select-address/', views.select_address, name='select_address'),
    path('add-address/', views.add_address, name='add_address'),
    path('edit-address/', views.edit_address, name='edit_address'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)