from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.account_overview, name='account_overview'),
    path('orders/', views.view_orders, name='view_orders'),
    path('find-order/', views.find_order, name='find_order'),
    path('order-info/int:<order_id>/', views.order_info, name='order_info'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)