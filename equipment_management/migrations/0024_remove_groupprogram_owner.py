# Generated by Django 5.1.1 on 2024-11-21 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_management', '0023_remove_software_purchase_date_groupprogram_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupprogram',
            name='owner',
        ),
    ]