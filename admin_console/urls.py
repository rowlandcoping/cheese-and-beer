from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.admin_console, name='admin_console'),
    path('view-messages/', views.view_messages, name='view_messages'),
    path('remove-message/<int:message_id>/', views.remove_message, name='remove_message'),
]
