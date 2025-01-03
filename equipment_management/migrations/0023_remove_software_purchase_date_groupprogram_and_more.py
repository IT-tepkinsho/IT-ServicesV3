# Generated by Django 5.1.1 on 2024-11-21 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_management', '0022_cameracctv'),
        ('user_management', '0002_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='software',
            name='purchase_date',
        ),
        migrations.CreateModel(
            name='GroupProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('license_key', models.CharField(blank=True, max_length=100, null=True)),
                ('equipment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='equipment_management.equipmenttype')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='program', to='user_management.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Program',
        ),
    ]
