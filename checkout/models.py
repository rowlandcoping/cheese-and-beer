import uuid
from django.db import models
from products.models import Product
from addresses.models import Addresses
from django.contrib.auth.models import User


class Order(models.Model):
    """
    This Model is for an individual order. It originates from the Boutique Ado
    tutorial site however it is not linked to a User Profile model, as I have
    created a seperate address management module which stores user details.
    It has also been customised a fair amount to reflect this.
    """
    order_number = models.CharField(
        max_length=32, null=False, editable=False)
    user_id = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    shipping_id = models.ForeignKey(
        Addresses, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.CharField(max_length=254, null=False, blank=False)
    full_name = models.CharField(max_length=254, null=False, blank=False)
    address_line_one = models.CharField(
        max_length=254, null=False, blank=False)
    address_line_two = models.CharField(max_length=254, null=True, blank=True)
    town_or_city = models.CharField(max_length=64, null=False, blank=False)
    county = models.CharField(max_length=32, null=False, blank=False)
    postcode = models.CharField(max_length=8, null=False, blank=False)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False)

    def _generate_order_number(self):
        """
        Generates an order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number. This
        originates from the Boutique Ado project. I have added a function
        to update the shipping address if the foreign key is updated on
        the back end and avoid any dissonance.
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
    """
    This model is for individual components of an order.
    It originates from the Boutique Ado project, but is not
    implemented in the same way.
    """
    order_id = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product_type = models.CharField()
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    item_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total and set product units sold.
        This originates from the Boutique Ado project.
        """
        self.item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order_id.order_number}'
