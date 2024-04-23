from django.db.models.signals import post_save
from django.dispatch import receiver
from checkout.models import OrderItems


@receiver(post_save, sender=OrderItems)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    This code is borrowed from Boutique Ado.
    """
    instance.product.units_sold()
