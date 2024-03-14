from django.urls import path
from . import views

urlpatterns = [
    path('add-cheese-catgory/', views.add_cheese_category, name='add_cheese_category'),
    path('add-beer-catgory/', views.add_beer_category, name='add_beer_category'),
    path('edit-catgories/', views.edit_categories, name='edit_categories'),
    path('edit-cheese-category/<int:category_id>/', views.edit_cheese_category, name='edit_cheese_category'),
    path('edit-beer-category/<int:category_id>/', views.edit_beer_category, name='edit_beer_category'),
]

