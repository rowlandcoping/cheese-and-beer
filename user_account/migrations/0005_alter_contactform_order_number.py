# Generated by Django 5.0.2 on 2024-04-22 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0004_contactform_delete_contact_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='order_number',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
