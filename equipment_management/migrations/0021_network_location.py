# Generated by Django 5.1.1 on 2024-11-21 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_management', '0020_alter_equipment_equipment_type_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
