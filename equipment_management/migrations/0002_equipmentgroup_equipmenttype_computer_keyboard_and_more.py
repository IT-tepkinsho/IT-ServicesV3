# Generated by Django 5.1.1 on 2024-11-01 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='equipment_types', to='equipment_management.equipmentgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_code', models.CharField(max_length=50, unique=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('processor', models.CharField(blank=True, max_length=50, null=True)),
                ('ram_size', models.IntegerField(default=4)),
                ('storage_size', models.IntegerField(default=512)),
                ('purchase_date', models.DateField()),
                ('equipment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computers', to='equipment_management.equipmenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_code', models.CharField(max_length=50, unique=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('layout', models.CharField(blank=True, max_length=20, null=True)),
                ('connection_type', models.CharField(blank=True, max_length=20, null=True)),
                ('purchase_date', models.DateField()),
                ('equipment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keyboards', to='equipment_management.equipmenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_code', models.CharField(max_length=50, unique=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('screen_size', models.IntegerField(default=24)),
                ('resolution', models.CharField(blank=True, max_length=50, null=True)),
                ('purchase_date', models.DateField()),
                ('equipment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monitors', to='equipment_management.equipmenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_code', models.CharField(max_length=50, unique=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('connection_type', models.CharField(blank=True, max_length=20, null=True)),
                ('purchase_date', models.DateField()),
                ('equipment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mice', to='equipment_management.equipmenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_code', models.CharField(max_length=50, unique=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('print_type', models.CharField(blank=True, max_length=20, null=True)),
                ('purchase_date', models.DateField()),
                ('equipment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printers', to='equipment_management.equipmenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('license_key', models.CharField(blank=True, max_length=100, null=True)),
                ('purchase_date', models.DateField()),
                ('equipment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='equipment_management.equipmenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_code', models.CharField(max_length=50, unique=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('cpu', models.CharField(blank=True, max_length=50, null=True)),
                ('ram_size', models.IntegerField()),
                ('storage_size', models.IntegerField()),
                ('purchase_date', models.DateField()),
                ('equipment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servers', to='equipment_management.equipmenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('version', models.CharField(blank=True, max_length=50, null=True)),
                ('license_key', models.CharField(blank=True, max_length=100, null=True)),
                ('purchase_date', models.DateField()),
                ('equipment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='software', to='equipment_management.equipmenttype')),
            ],
        ),
    ]