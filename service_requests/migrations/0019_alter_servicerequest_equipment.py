# Generated by Django 5.1.1 on 2024-11-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0018_repairupdatelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='equipment',
            field=models.CharField(max_length=50),
        ),
    ]
