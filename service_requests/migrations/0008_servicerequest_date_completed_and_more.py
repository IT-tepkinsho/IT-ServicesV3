# Generated by Django 5.1.1 on 2024-10-24 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0007_remove_servicerequest_request_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='date_completed',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='date_received',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='method_of_repair',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='operator',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='total_repair_time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]