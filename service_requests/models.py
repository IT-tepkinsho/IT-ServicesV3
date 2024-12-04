from django.db import models
from repair_management.models import RepairType, RepairTopic # เชื่อมโยงกับโมเดล RepairType, RepairTopic
from user_management.models import Department, User # เชื่อมโยงกับโมเดล Department, User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
    
class ServiceRequestConfig(models.Model):
    base_year = models.IntegerField(default=67)  # Starting year
    last_number = models.IntegerField(default=0)  # Last number used

    def reset_last_number(self):
        self.last_number = 0
        self.save()

    def get_next_request_number(self):
        self.last_number += 1
        self.save()
        # Format last_number as a four-digit string
        return f'MIT{self.base_year}-{self.last_number:04d}'
    

class RequestStatus(models.Model):
    name = models.CharField(max_length=100)  # ชื่อสถานะ

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    
    service_request_number = models.CharField(max_length=20, unique=True, blank=True, null=True)  # เลขที่ใบแจ้งซ่อม
    repair_type = models.ForeignKey(RepairType, on_delete=models.SET_NULL, null=True)  # ประเภทการซ่อม (เปลี่ยนเป็น ForeignKey)
    repair_title = models.ForeignKey(RepairTopic, on_delete=models.SET_NULL, null=True)  # หัวข้อการซ่อม (เปลี่ยนเป็น ForeignKey)
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # ผู้แจ้ง
    user_department = models.CharField(max_length=50, null=True)  # หน่วยงาน
    user_contact = models.CharField(max_length=20, null=True)  # เบอร์ติดต่อ
    attached_file = models.FileField(upload_to='service_requests/files/', null=True, blank=True)  # แนบไฟล์
    request_description = models.TextField()  # ปัญหาและอาการ
    request_date = models.DateTimeField(auto_now_add=True)  # วันที่เวลาที่แจ้ง
    repair_status = models.ForeignKey(RequestStatus, on_delete=models.SET_NULL, null=True, default=None)  # สถานะการแจ้งซ่อม
    repair_by = models.CharField(max_length=50, null=True, blank=True, choices=[
        ('it_repair', 'ซ่อมโดยฝ่ายเทคโนโลยีสารสนเทศ'),
        ('external_repair', 'ส่งซ่อม/ส่งเคลม'),
    ])

    equipment = models.CharField(max_length=50)  # รหัสอุปกรณ์
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ค่าใช้จ่าย", null=True, blank=True)
    change_device = models.BooleanField(default=False, verbose_name="เปลี่ยนอุปกรณ์")
    equipment_new = models.CharField(max_length=100, verbose_name="รหัสอุปกรณ์ใหม่", null=True, blank=True)
    method_of_repair = models.TextField(null=True, blank=True, default='')  # วิธีดำเนินการ
    date_received = models.DateTimeField(null=True, blank=True)  # วันที่รับงาน
    date_completed = models.DateTimeField(null=True, blank=True)  # วันที่ซ่อมเสร็จ
    total_repair_time = models.DurationField(null=True, blank=True)  # รวมเวลาซ่อม
    operator = models.CharField(max_length=50, null=True, blank=True, default='')  # ผู้ดำเนินการ


    def save(self, *args, **kwargs):
        # Set service_request_number if it's not set
        if not self.service_request_number:
            try:
                config = ServiceRequestConfig.objects.first()  # Assuming a single instance
                # Check if the current year is different from the base year
                current_year = (timezone.now().year + 543) % 100  # Get last two digits of the year
                if config.base_year != current_year:
                    config.base_year = current_year
                    config.last_number = 0  # Reset the last number for the new year
                    config.save()
                self.service_request_number = config.get_next_request_number()
            except ObjectDoesNotExist:
                raise ValueError("ServiceRequestConfig instance not found.")
            
                # ตั้งค่า repair_status ให้เป็น 'pending' ถ้ายังไม่ถูกตั้งค่า
        if self.repair_status is None:
            try:
                self.repair_status = RequestStatus.objects.get(name='pending')  # ค้นหาค่าจากโมเดล RequestStatus
            except ObjectDoesNotExist:
                raise ValueError("RequestStatus instance with name 'pending' not found.")
        
        # คำนวณ total_repair_time
        if self.date_received and self.date_completed:
            self.total_repair_time = self.date_completed - self.date_received
            
        super(ServiceRequest, self).save(*args, **kwargs) 
    
    def __str__(self):
        return f"{self.service_request_number}"
    

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
    

class RepairUpdateLog(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='repair_updates')  # ลิงก์กับ ServiceRequest
    update_datetime = models.DateTimeField(default=timezone.now)  # วันที่เวลาที่อัพเดต
    total_repair_time = models.DurationField(null=True, blank=True)  # เวลารวมในการซ่อม
    details = models.TextField(null=True)  # รายละเอียดของการอัพเดต

    def __str__(self):
        return f"Repair Update for {self.service_request.service_request_number} at {self.update_datetime}"

    def save(self, *args, **kwargs):
            # คำนวณ total_repair_time เมื่อบันทึก
            if self.service_request and self.service_request.date_received:
                self.total_repair_time = self.update_datetime - self.service_request.date_received
            super().save(*args, **kwargs)