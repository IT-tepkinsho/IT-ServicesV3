# Generated by Django 5.1.1 on 2024-11-26 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_management', '0031_software_computer_alter_computer_software'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='software',
        ),
        migrations.AddField(
            model_name='computer',
            name='software',
            field=models.ManyToManyField(blank=True, related_name='computers', to='equipment_management.software'),
        ),
    ]