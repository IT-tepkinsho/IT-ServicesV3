# Generated by Django 5.1.1 on 2024-10-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0009_alter_servicerequest_date_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='method_of_repair',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='operator',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='total_repair_time',
            field=models.DurationField(blank=True, default='', null=True),
        ),
    ]