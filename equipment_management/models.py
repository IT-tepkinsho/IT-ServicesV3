from asyncio import Condition
from ipaddress import ip_address
from django.db import models
from repair_management.models import Vendor
from user_management.models import User

class EquipmentGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class EquipmentType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    group = models.ForeignKey(EquipmentGroup, on_delete=models.CASCADE, default=1, related_name='equipment_types')

    def __str__(self):
        return self.name

class EquipmentStatus(models.Model):
    name = models.CharField(max_length=255, verbose_name="สถานะอุปกรณ์")

    def __str__(self):
        return self.name

class EquipmentCondition(models.Model):
    name = models.CharField(max_length=255, verbose_name="สภาพอุปกรณ์")

    def __str__(self):
        return self.name

class Monitor(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    serial_number = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    warranty = models.DateField()
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='monitors')
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    condition = models.ForeignKey(EquipmentCondition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สภาพอุปกรณ์")
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='monitors')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='monitors')

    def __str__(self):
        return f" {self.equipment_code} ({self.brand})"


class Mouse(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    connection_type = models.CharField(max_length=20, null=True, blank=True)  # Wired/Wireless
    purchase_date = models.DateField()
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='mouse')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='mouse')

    def __str__(self):
        return f" {self.equipment_code} ({self.name})"

class Keyboard(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    layout = models.CharField(max_length=20, null=True, blank=True)  # QWERTY, AZERTY, etc.
    connection_type = models.CharField(max_length=20, null=True, blank=True)  # Wired/Wireless
    purchase_date = models.DateField()
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='keyboards')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='keyboards')

    def __str__(self):
        return f" {self.equipment_code} ({self.name})"

class Printer(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    serial_number = models.CharField(max_length=50, null=True, blank=True)
    print_type = models.CharField(max_length=20, null=True, blank=True)  # Inkjet/Laser
    purchase_date = models.DateField()
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='printers')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='printers')

    def __str__(self):
        return f" {self.equipment_code} ({self.name})"
    
class Scanner(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    serial_number = models.CharField(max_length=50, null=True, blank=True)
    scan_type = models.CharField(max_length=20, null=True, blank=True)  # Inkjet/Laser
    purchase_date = models.DateField()
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='scanners')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='scanners')

    def __str__(self):
        return f" {self.equipment_code} ({self.name})"

class Server(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    cpu = models.CharField(max_length=50, null=True, blank=True)
    ram_size = models.IntegerField()  # in GB
    storage_size = models.IntegerField()  # in GB
    purchase_date = models.DateField()
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='servers')


    def __str__(self):
        return f" {self.equipment_code} ({self.name})"
    
class Ups(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    purchase_date = models.DateField()
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='ups')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='ups')

    def __str__(self):
        return f" {self.equipment_code} ({self.name})"


class Software(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    version = models.CharField(max_length=50, null=True, blank=True)
    license_key = models.CharField(max_length=100, null=True, blank=True)
    purchase_date = models.DateField()
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='software')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='software')

    def __str__(self):
        return f" {self.equipment_code} ({self.name})"

class Program(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    license_key = models.CharField(max_length=100, null=True, blank=True)
    purchase_date = models.DateField()
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='programs')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='programs')

    def __str__(self):
        return f" {self.equipment_code} ({self.name})"
    
class Equipment(models.Model):
    EQUIPMENT_TYPE_CHOICES = [
        ('notebooke', 'Notebook'),
        ('computer', 'Computer'),
        ('printer', 'Printer'),
        ('network_device', 'Network Device'),
    ]
    
    name = models.CharField(max_length=100)
    equipment_type = models.CharField(choices=EQUIPMENT_TYPE_CHOICES, max_length=50)
    serial_number = models.CharField(max_length=50, unique=True)
    purchase_date = models.DateField()
    warranty_expiration = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Computer(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    spec = models.TextField(default='N/A')
    brand = models.CharField(max_length=50, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    internet_connection = models.BooleanField(default=False, verbose_name="เชื่อมต่อ Internet")
    equipment_status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    equipment_condition = models.ForeignKey(EquipmentCondition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สภาพอุปกรณ์")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, verbose_name="vendor")
    other = models.TextField(null=True, blank=True, verbose_name="อื่นๆ")
    monitor = models.ForeignKey(Monitor, on_delete=models.SET_NULL, null=True, verbose_name="monitor")
    monitor_model = models.CharField(max_length=255, null=True, blank=True)
    keyboard = models.ForeignKey(Keyboard, on_delete=models.SET_NULL, null=True, verbose_name="keyboard")
    keyboard_brand = models.CharField(max_length=255, null=True, blank=True)
    mouse = models.ForeignKey(Mouse, on_delete=models.SET_NULL, null=True, verbose_name="mouse")
    mouse_brand = models.CharField(max_length=255, null=True, blank=True)
    printer = models.ForeignKey(Printer, on_delete=models.SET_NULL, null=True, verbose_name="printer")
    printer_model = models.CharField(max_length=255, null=True, blank=True)
    ups = models.ForeignKey(Ups, on_delete=models.SET_NULL, null=True, verbose_name="UPS")
    ups_model = models.CharField(max_length=255, null=True, blank=True)
    scanner = models.ForeignKey(Scanner, on_delete=models.SET_NULL, null=True, verbose_name="Scanner")
    scanner_model = models.CharField(max_length=255, null=True, blank=True)
    software = models.ForeignKey(Software, on_delete=models.SET_NULL, null=True, verbose_name="software license")
    software_name = models.CharField(max_length=255, null=True, blank=True)
    license_key = models.CharField(max_length=255, null=True, blank=True)
    purchase_date = models.DateField()
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.SET_NULL, null=True, blank=True, related_name='computers')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='computers')

    def __str__(self):
        return f" {self.equipment_code} ({self.owner})"


