# Generated by Django 5.1.1 on 2024-12-03 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0022_servicerequest_change_device_servicerequest_cost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repairupdatelog',
            name='change_device',
        ),
        migrations.RemoveField(
            model_name='repairupdatelog',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='repairupdatelog',
            name='equipment_new',
        ),
        migrations.RemoveField(
            model_name='repairupdatelog',
            name='equipment_old',
        ),
        migrations.RemoveField(
            model_name='repairupdatelog',
            name='operator',
        ),
    ]
