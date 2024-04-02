# Generated by Django 5.0.2 on 2024-04-02 01:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0002_alter_addresses_address_line_two'),
        ('checkout', '0003_delete_addresses'),
        ('products', '0018_product_displayed'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=254)),
                ('address_line_one', models.CharField(max_length=254)),
                ('address_line_two', models.CharField(blank=True, max_length=254, null=True)),
                ('town_or_city', models.CharField(max_length=64)),
                ('county', models.CharField(max_length=32)),
                ('postcode', models.CharField(max_length=8)),
                ('order_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('items_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('other_costs', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('shipping_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addresses.addresses')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField()),
                ('quantity', models.IntegerField(default=0)),
                ('item_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
        ),
    ]
