# Generated by Django 5.1.4 on 2024-12-06 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_requests', '0026_rename_vendor_repairclaim_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='feedback_comment',
            field=models.TextField(blank=True, null=True, verbose_name='ความคิดเห็นเพิ่มเติม'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='satisfaction_score',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '1 ดาว'), (2, '2 ดาว'), (3, '3 ดาว'), (4, '4 ดาว'), (5, '5 ดาว')], null=True, verbose_name='คะแนนความพึงพอใจ'),
        ),
    ]
