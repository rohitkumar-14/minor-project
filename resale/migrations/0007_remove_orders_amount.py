# Generated by Django 4.1.1 on 2023-05-23 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resale', '0006_remove_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
    ]
