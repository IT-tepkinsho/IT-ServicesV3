# Generated by Django 5.1.1 on 2024-11-06 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=50, unique=True)),
                ('vendor_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]