from django.db import models
from equipment_management.models import Equipment  # เชื่อมโยงกับโมเดล Equipment

class ServiceRequest(models.Model):
    REQUEST_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    repair_type = models.CharField(max_length=100, null=True)  # ประเภทการซ่อม
    repair_title = models.CharField(max_length=200, null=True)  # หัวข้อการซ่อม
    user_name = models.CharField(max_length=100, null=True)  # ผู้แจ้ง
    user_department = models.CharField(max_length=100, null=True)  # หน่วยงาน
    user_contact = models.CharField(max_length=20, null=True)  # เบอร์ติดต่อ
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)  # รหัสอุปกรณ์
    attached_file = models.FileField(upload_to='service_requests/files/', null=True, blank=True)  # แนบไฟล์
    request_description = models.TextField()  # ปัญหาและอาการ
    request_date = models.DateTimeField(auto_now_add=True)  # วันที่เวลาที่แจ้ง
    request_status = models.CharField(max_length=50, choices=REQUEST_STATUS_CHOICES, default='pending')  # สถานะการแจ้งซ่อม
    repair_by = models.CharField(max_length=50, choices=[
        ('do_it_yourself', 'ซ่อมโดยฝ่ายเทคโนโลยีสารสนเทศ'),
        ('claim', 'ส่งเคลม'),
    ], default='do_it_yourself')

    def __str__(self):
        return f"Service Request for {self.equipment} by {self.user_name} - Status: {self.request_status}"


class Repair(models.Model):
    request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    repair_details = models.TextField()
    repair_date = models.DateTimeField(auto_now_add=True)
    repair_status = models.CharField(max_length=50, choices=[
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    ])

    def __str__(self):
        return f"Repair for {self.request.equipment.name}"


class Claim(models.Model):
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE)
    claim_description = models.TextField()
    claim_status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ])
    claim_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Claim for {self.repair.request.equipment.name} - Status: {self.claim_status}"


class ActivityLog(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    action_taken = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Activity for {self.service_request.equipment.name} - Action: {self.action_taken}"

