# Generated by Django 5.0.2 on 2024-03-28 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresses',
            name='address_line_two',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]