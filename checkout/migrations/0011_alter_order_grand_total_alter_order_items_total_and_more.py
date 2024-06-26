# Generated by Django 5.0.2 on 2024-04-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_alter_orderitems_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='grand_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='items_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='item_total',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
