from django.db import models
from django.contrib.auth.models import User


class Addresses(models.Model):
    """
    This model is for the user address management module which also integrates
    with the checkout view
    """
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=254, null=False, blank=False)
    address_line_one = models.CharField(
        max_length=254, null=False, blank=False)
    address_line_two = models.CharField(max_length=254, null=True, blank=True)
    town_or_city = models.CharField(max_length=64, null=False, blank=False)
    county = models.CharField(max_length=32, null=False, blank=False)
    postcode = models.CharField(max_length=8, null=False, blank=False)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.address_line_one
