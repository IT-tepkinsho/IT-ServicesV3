# Generated by Django 5.1.1 on 2024-11-01 07:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_management', '0002_equipmentgroup_equipmenttype_computer_keyboard_and_more'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='computers', to='user_management.user'),
        ),
        migrations.AddField(
            model_name='keyboard',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='keyboard',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='keyboards', to='user_management.user'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='monitor',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='monitors', to='user_management.user'),
        ),
        migrations.AddField(
            model_name='mouse',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mouse',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mouse', to='user_management.user'),
        ),
        migrations.AddField(
            model_name='printer',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='printer',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='printers', to='user_management.user'),
        ),
        migrations.AddField(
            model_name='program',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programs', to='user_management.user'),
        ),
        migrations.AddField(
            model_name='server',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='software',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='software', to='user_management.user'),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='equipment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mouse', to='equipment_management.equipmenttype'),
        ),
    ]
