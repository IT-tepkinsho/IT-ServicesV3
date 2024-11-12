from django.db import models

class RepairType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RepairTopic(models.Model):
    name = models.CharField(max_length=100)
    repair_type = models.ForeignKey(RepairType, related_name='topics', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Vendor(models.Model):
    vendor_code = models.CharField(max_length=50, unique=True)
    vendor_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f" {self.vendor_code} ({self.vendor_name})"