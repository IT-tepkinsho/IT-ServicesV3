# Generated by Django 5.1.1 on 2024-11-12 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_management', '0014_remove_keyboard_layout_remove_keyboard_name_and_more'),
        ('repair_management', '0002_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='purchase_date',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='serial_number',
        ),
        migrations.AddField(
            model_name='printer',
            name='condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipment_management.equipmentcondition', verbose_name='สภาพอุปกรณ์'),
        ),
        migrations.AddField(
            model_name='printer',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='printer',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipment_management.equipmentstatus', verbose_name='สถานะอุปกรณ์'),
        ),
        migrations.AddField(
            model_name='printer',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='printers', to='repair_management.vendor'),
        ),
        migrations.AddField(
            model_name='printer',
            name='warranty',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='print_type',
            field=models.CharField(blank=True, choices=[('inkjet', 'Inkjet'), ('laser', 'Laser'), ('dotmatrix', 'Dotmatrix')], max_length=20, null=True),
        ),
    ]