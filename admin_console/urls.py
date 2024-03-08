from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.admin_console, name='admin_console')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
