from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('confirmation/<order_number>', views.confirmation, name='confirmation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)