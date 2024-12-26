from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ServiceRequest


@receiver(post_save, sender=ServiceRequest)
def send_feedback_email_on_completed(sender, instance, **kwargs):
    """ส่งอีเมลเมื่อสถานะเป็น completed และยังไม่ได้ประเมิน"""
    if instance.repair_status and instance.repair_status.name == "completed" and not instance.feedback_submitted:
        instance.send_feedback_email()