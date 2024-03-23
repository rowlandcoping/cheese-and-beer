from django.urls import path
from . import views

urlpatterns = [
    path('view-products/', views.view_results, name='view_results'),
]