# Generated by Django 5.1.4 on 2024-12-18 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment_management', '0040_alter_computer_software'),
        ('user_management', '0004_alter_user_nameen_alter_user_nameth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='computer_owners', to='user_management.user'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='software',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='computers', to='equipment_management.software', verbose_name='software license'),
        ),
        migrations.AlterField(
            model_name='software',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='ราคา'),
        ),
        migrations.AlterField(
            model_name='software',
            name='license_key',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='license key'),
        ),
        migrations.AlterField(
            model_name='software',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ชื่อซอฟต์แวร์'),
        ),
        migrations.AlterField(
            model_name='software',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='software_owners', to='user_management.user', verbose_name='ผู้ครอบครอง'),
        ),
        migrations.AlterField(
            model_name='software',
            name='version',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='เวอร์ชัน'),
        ),
    ]