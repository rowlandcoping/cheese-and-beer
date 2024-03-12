from django.db import models

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
    pairs_with = models.ManyToManyField(BeerCategory, blank=True)

    def __str__(self):
        return self.name