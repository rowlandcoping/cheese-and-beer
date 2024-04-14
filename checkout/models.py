import uuid
from django.db import models
from products.models import Product
from addresses.models import Addresses
from django.contrib.auth.models import User


class Order(models.Model):
    readonly_fields = ["order_number","order_date","items_total", "delivery_cost", "grand_total", "stripe_pid"] 
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    shipping_id = models.ForeignKey(Addresses, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.CharField(max_length=254, null=False, blank=False)
    full_name = models.CharField(max_length=254, null=False, blank=False)    
    address_line_one = models.CharField(max_length=254, null=False, blank=False)
    address_line_two = models.CharField(max_length=254, null=True, blank=True)
    town_or_city = models.CharField(max_length=64, null=False, blank=False)
    county = models.CharField(max_length=32, null=False, blank=False)
    postcode = models.CharField(max_length=8, null=False, blank=False)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False)


    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        if self.shipping_id:
            self.full_name = self.shipping_id.full_name
            self.address_line_one = self.shipping_id.address_line_one
            self.address_line_two = self.shipping_id.address_line_two
            self.town_or_city = self.shipping_id.town_or_city
            self.county = self.shipping_id.county
            self.postcode = self.shipping_id.postcode
        super().save(*args, **kwargs)


    def __str__(self):
        return self.order_number


class OrderItems(models.Model):
    readonly_fields = ["order_id", "product_type","product", "price", "quantity", "item_total"] 
    order_id = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product_type = models.CharField()
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    # discounts = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total and set product units sold.
        """
        self.item_total = self.product.price * self.quantity        
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.product.name} on order {self.order_id.order_number}'