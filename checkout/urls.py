from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .webhooks import webhook
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'confirmation/<order_number>',
        views.confirmation, name='confirmation'),
    path('wh/', webhook, name='webhook'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
