# Generated by Django 5.0.2 on 2024-03-20 16:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_product_price_alter_product_price_per_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_number',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=254),
            preserve_default=False,
        ),
    ]
