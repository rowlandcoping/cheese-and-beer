from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add-basket/', views.add_to_basket, name='add_to_basket'),
    path('buy-now/', views.buy_now, name='buy_now'),
    path('basket/', views.view_basket, name='view_basket'),
    path('update_basket/', views.update_basket, name='update_basket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
