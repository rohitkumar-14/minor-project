# Generated by Django 4.1.1 on 2023-05-25 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resale', '0008_rename_zip_code_orders_pin_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='pin_code',
            new_name='zip_code',
        ),
    ]