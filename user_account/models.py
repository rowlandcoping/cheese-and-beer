from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    @receiver(pre_save, sender=User)
    def populate_user(sender, instance, **kwargs):
        user_email = instance.email
        username = user_email
        while User.objects.exclude(pk=instance.pk).filter(username=username).exists():
            n += 1
        instance.username = username