# Generated by Django 5.1.4 on 2024-12-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0027_servicerequest_feedback_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='feedback_submitted',
            field=models.BooleanField(default=False, verbose_name='ประเมินเสร็จแล้ว'),
        ),
    ]
