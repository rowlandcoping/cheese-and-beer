from django.urls import path
from . import views

urlpatterns = [
    path(
        'add-cheese-category/',
        views.add_cheese_category,
        name='add_cheese_category'
        ),
    path(
        'add-beer-category/',
        views.add_beer_category,
        name='add_beer_category'
        ),
    path('add-cheese/', views.add_cheese, name='add_cheese'),
    path('add-beer/', views.add_beer, name='add_beer'),
    path('products', views.add_product, name='add_product'),
    path('edit-product/', views.edit_product, name='edit_product'),
    path(
        'product-edit/<int:product_id>/',
        views.product_edit,
        name='product_edit'
        ),
    path('edit-catgories/', views.edit_categories, name='edit_categories'),
    path(
        'edit-cheese-category/<int:category_id>/',
        views.edit_cheese_category,
        name='edit_cheese_category'
        ),
    path(
        'edit-beer-category/<int:category_id>/',
        views.edit_beer_category,
        name='edit_beer_category'
        ),
    path(
        'delete-product/<int:product_id>/',
        views.delete_product,
        name='delete_product'
        ),
    path(
        'publish-product/<int:product_id>/',
        views.product_publish,
        name='product_publish'
        ),
    path(
        'unpublish-product/<int:product_id>/',
        views.product_unpublish,
        name='product_unpublish'
        ),
]
