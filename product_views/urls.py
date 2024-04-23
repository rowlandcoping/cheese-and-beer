from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_results, name='view_results'),
    path(
        'product-detail/<int:product_id>/',
        views.product_detail, name='product_detail'),
]
