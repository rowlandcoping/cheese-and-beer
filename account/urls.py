from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.account_overview, name='account_overview'),
    path('orders', views.view_orders, name='view_orders'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)