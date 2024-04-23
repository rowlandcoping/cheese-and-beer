from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from datetime import datetime
from products.models import Product
from checkout.models import Order
from django.dispatch import receiver
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.db import models


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    @receiver(pre_save, sender=User)
    def populate_user(sender, instance, **kwargs):
        """
        This is a customisation of the user model to prevent the user from
        having to submit an username. Instead prior to save the username is
        set to the user's e-mail address. This speeds up sign-up and avoids
        the overhead of users forgetting their usernames.
        """
        unm = instance.email
        pki = instance.pk
        while User.objects.exclude(pk=pki).filter(username=unm).exists():
            n += 1
        instance.username = unm


class Wishlist(models.Model):
    """
    This model stores products users wish to save on their wishlists.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'{self.product.name}'


class ContactForm(models.Model):
    """
    This model stores messages from customers for future action.
    """
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    order = models.ForeignKey(
        Order, null=True, blank=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=254, null=False, blank=False)
    order_number = models.CharField(
        max_length=32, null=True, blank=True, editable=True)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.subject
