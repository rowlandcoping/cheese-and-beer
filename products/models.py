from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class BeerCategory(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.CharField(max_length=254, null=True, blank=True)
    image_alt = models.CharField(max_length=1024, null=True, blank=True)


    def __str__(self):
        return self.name
   

class CheeseCategory(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.CharField(max_length=254, null=True, blank=True)
    image_alt = models.CharField(max_length=1024, null=True, blank=True)
    pairs_with = models.ManyToManyField(BeerCategory, related_name="cheese", blank=True)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    #common fields
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=6)
    description = models.TextField()
    variety = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.CharField(max_length=254, null=True, blank=True)
    image_alt = models.CharField(max_length=1024, null=True, blank=True)
    country_origin = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        choices=CountryField().choices
    )
    # fields specific to cheese
    cheese_category = models.ForeignKey('CheeseCategory', null=True, blank=True, on_delete=models.SET_NULL)
    # fields specific to beer
    beer_category = models.ForeignKey('BeerCategory', null=True, blank=True, on_delete=models.SET_NULL)
    alcohol_content = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

   
    


    def __str__(self):
        return self.name