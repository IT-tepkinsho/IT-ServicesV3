# Generated by Django 5.1.1 on 2024-11-12 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_management', '0010_remove_mouse_connection_type_remove_mouse_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mouse',
            name='status',
        ),
        migrations.RemoveField(
            model_name='mouse',
            name='vendor',
        ),
    ]