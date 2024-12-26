
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
    warranty = models.DateField(null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='monitors')
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    condition = models.ForeignKey(EquipmentCondition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สภาพอุปกรณ์")
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='monitors')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='monitors')

    def __str__(self):
        return f" {self.equipment_code} ({self.brand})"


class Mouse(models.Model):
    CONNECTION_TYPE_CHOICES = [
        ('wired', 'Wired'),
        ('wireless', 'Wireless'),
    ]

    equipment_code = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    connection_type = models.CharField(choices=CONNECTION_TYPE_CHOICES, max_length=20, null=True, blank=True)  # Wired/Wireless
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    condition = models.ForeignKey(EquipmentCondition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สภาพอุปกรณ์")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='mouses')
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='mouses')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='mouses')

    def __str__(self):
        return f" {self.equipment_code} ({self.brand})"

class Keyboard(models.Model):
    CONNECTION_TYPE_CHOICES = [
        ('wired', 'Wired'),
        ('wireless', 'Wireless'),
    ]
        
    equipment_code = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    connection_type = models.CharField(choices=CONNECTION_TYPE_CHOICES, max_length=20, null=True, blank=True)  # Wired/Wireless
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    condition = models.ForeignKey(EquipmentCondition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สภาพอุปกรณ์")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='keyboards')
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='keyboards')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='keyboards')

    def __str__(self):
        return f" {self.equipment_code} ({self.brand})"

class Printer(models.Model):
    PRINT_TYPE_CHOICES = [
        ('inkjet', 'Inkjet'),
        ('laser', 'Laser'),
        ('dotmatrix', 'Dotmatrix')
    ]
        
    equipment_code = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    print_type = models.CharField(choices=PRINT_TYPE_CHOICES, max_length=20, null=True, blank=True)  # Inkjet/Laser
    ip_address = models.CharField(max_length=50, null=True, blank=True, verbose_name="IP Address")
    warranty = models.DateField(null=True, blank=True)
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    condition = models.ForeignKey(EquipmentCondition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สภาพอุปกรณ์")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='printers')
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='printers')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='printers')
    
    def __str__(self):
        return f" {self.equipment_code} ({self.brand})"
    
class Scanner(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    warranty = models.DateField(null=True, blank=True)
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    condition = models.ForeignKey(EquipmentCondition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สภาพอุปกรณ์")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='scanners')
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='scanners')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='scanners')
    def __str__(self):
        return f" {self.equipment_code} ({self.brand})"

class Server(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    spec = models.TextField(default='N/A')
    location = models.CharField(max_length=100, null=True, blank=True)
    ip_address = models.CharField(max_length=50, null=True, blank=True)
    serial_number = models.CharField(max_length=50, null=True, blank=True)
    warranty = models.DateField(null=True, blank=True)
    ibm_warranty = models.DateField(null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='servers')
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='servers')

    def __str__(self):
        return f" {self.equipment_code} ({self.location})"
    
class Ups(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    warranty = models.DateField(null=True, blank=True)
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    condition = models.ForeignKey(EquipmentCondition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สภาพอุปกรณ์")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='upses')
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='upses')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='upses')
    
    def __str__(self):
        return f" {self.equipment_code} ({self.brand})"

class GroupProgram(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class SoftwareType(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    group = models.ForeignKey(GroupProgram, on_delete=models.SET_NULL, null=True, blank=True, related_name='software_types')


class Software(models.Model):
    STATUS_CHOICES = [
        ('enable', 'enable'),
        ('disable', 'disable'),
    ]
        
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    version = models.CharField(max_length=50, null=True, blank=True)
    license_key = models.CharField(max_length=100, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    computer = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True, blank=True, related_name='install_software')
    group_program = models.ForeignKey(GroupProgram, on_delete=models.SET_NULL, null=True, blank=True, related_name='software')
    software_type = models.ForeignKey(SoftwareType, on_delete=models.SET_NULL, null=True, blank=True, related_name='software')
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, null=True, blank=True) #สถานะ software
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='software')
    other = models.TextField(null=True, blank=True, verbose_name='หมายเหตุ')

    def __str__(self):
        return f" {self.equipment_code} ({self.name})"


class Equipment(models.Model):
    EQUIPMENT_TYPE_CHOICES = [
        ('notebook', 'Notebook'),
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
    ip_address = models.CharField(max_length=50, null=True, blank=True)
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
    software = models.ManyToManyField(Software, blank=True, related_name='software_computers')
    program = models.CharField(max_length=255, null=True, blank=True, verbose_name="โปรแกรมพิเศษ")
    purchase_date = models.DateField(null=True, blank=True)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.SET_NULL, null=True, blank=True, related_name='computers')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='computers')
    department = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f" {self.equipment_code}"

class Network(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ip_address = models.CharField(max_length=50, null=True, blank=True)
    serial_number = models.CharField(max_length=50, null=True, blank=True)
    warranty = models.DateField(null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='networks')
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    location = models.CharField(max_length=100, null=True, blank=True)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='networks')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='networks')

    def __str__(self):
        return f" {self.equipment_code} ({self.name})"
    
class CameraCCTV(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ip_address = models.CharField(max_length=50, null=True, blank=True)
    warranty = models.DateField(null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='cctvs')
    condition = models.ForeignKey(EquipmentCondition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สภาพอุปกรณ์")
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='cctvs')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='cctvs')

class Tablet(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ip_address = models.CharField(max_length=50, null=True, blank=True)
    warranty = models.DateField(null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='tablets')
    condition = models.ForeignKey(EquipmentCondition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สภาพอุปกรณ์")
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='tablets')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tablets')
    department = models.CharField(max_length=50, null=True, blank=True)

class Other(models.Model):
    equipment_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ip_address = models.CharField(max_length=50, null=True, blank=True)
    warranty = models.DateField(null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='others')
    condition = models.ForeignKey(EquipmentCondition, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สภาพอุปกรณ์")
    status = models.ForeignKey(EquipmentStatus, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="สถานะอุปกรณ์")
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='others')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='others')
    department = models.CharField(max_length=50, null=True, blank=True)
