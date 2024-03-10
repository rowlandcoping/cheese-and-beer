from django.db import models

# Create your models here.

class cheese_category(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()


    def __str__(self):
        return self.name
    

class beer_category(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    pairs_with = models.ManyToManyField(cheese_category, blank=True) 


    def __str__(self):
        return self.name