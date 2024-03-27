from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Addresses(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=254)
    address_line_one = models.CharField(max_length=254)
    address_line_two = models.CharField(max_length=254)
    town_or_city = models.CharField(max_length=64)
    county = models.CharField(max_length=32)
    postcode = models.CharField(max_length=8)
    default = models.BooleanField(default=False)


    def __str__(self):
        return self.name