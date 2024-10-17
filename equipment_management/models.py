from django.db import models

class Equipment(models.Model):
    EQUIPMENT_TYPE_CHOICES = [
        ('notebooke', 'Notebook'),
        ('computer', 'Computer'),
        ('printer', 'Printer'),
        ('network_device', 'Network Device'),
        # เพิ่มประเภทอุปกรณ์อื่น ๆ ตามต้องการ
    ]

    name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=50, choices=EQUIPMENT_TYPE_CHOICES)
    serial_number = models.CharField(max_length=50, unique=True)
    purchase_date = models.DateField()
    warranty_expiration = models.DateField()
    status = models.BooleanField(default=True)  # True: Active, False: Inactive

    def __str__(self):
        return f"{self.name} ({self.serial_number})"
