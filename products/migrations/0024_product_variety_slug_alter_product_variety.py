# Generated by Django 5.0.2 on 2024-04-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_remove_product_on_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variety_slug',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='variety',
            field=models.CharField(max_length=52),
        ),
    ]
