# Generated by Django 5.0.2 on 2024-04-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_product_texture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='units_sold',
            field=models.IntegerField(default=0),
        ),
    ]
