# Generated by Django 5.0.2 on 2024-03-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beer_category',
            name='pairs_with',
        ),
        migrations.AddField(
            model_name='beer_category',
            name='image_url',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='cheese_category',
            name='image_url',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='cheese_category',
            name='pairs_with',
            field=models.ManyToManyField(blank=True, to='products.beer_category'),
        ),
    ]
