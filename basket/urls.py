from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add-basket/', views.add_to_basket, name='add_to_basket'),
    path('buy-now/', views.buy_now, name='buy_now'),
    path('', views.view_basket, name='view_basket'),
    path('update_basket/', views.update_basket, name='update_basket'),
    path('remove_item/', views.remove_item, name='remove_item'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
