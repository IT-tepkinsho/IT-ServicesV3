from django.contrib import admin
from .models import (EquipmentCondition, EquipmentGroup, EquipmentStatus, EquipmentType, Computer, Monitor, Mouse,
                      Keyboard, Printer, Server, Software, Program, Equipment, Scanner, Ups)

# Register the EquipmentGroup model
@admin.register(EquipmentGroup)
class EquipmentGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register the EquipmentType model
@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'group')
    search_fields = ('name',)
    list_filter = ('group',)

# Register the Computer model
@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'spec', 'brand', 'vendor', 'owner', 'purchase_date', 'equipment_type', 'equipment_status')
    search_fields = ('equipment_code', 'brand', 'spec', 'vendor')
    list_filter = ('equipment_type',)

# Register the Monitor model
@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'brand', 'model', 'serial_number', 'cost', 'warranty', 'vendor', 'owner', 'status', 'condition')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Mouse model
@admin.register(Mouse)
class MouseAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'connection_type', 'purchase_date', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Keyboard model
@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'layout', 'connection_type', 'purchase_date', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Printer model
@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'print_type', 'purchase_date', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Scanner model
@admin.register(Scanner)
class ScannerAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'scan_type', 'purchase_date', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Server model
@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'cpu', 'ram_size', 'storage_size', 'purchase_date', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Ups model
@admin.register(Ups)
class UpsAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'purchase_date', 'equipment_type', 'owner')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Software model
@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'version', 'license_key', 'purchase_date', 'equipment_type')
    search_fields = ('equipment_code', 'name', 'version')
    list_filter = ('equipment_type',)

# Register the Program model
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'license_key', 'purchase_date', 'equipment_type')
    search_fields = ('equipment_code', 'name')
    list_filter = ('equipment_type',)

# Register the Equipment model
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'equipment_type', 'serial_number', 'purchase_date', 'warranty_expiration', 'status')
    search_fields = ('name', 'serial_number')
    list_filter = ('equipment_type', 'status')


@admin.register(EquipmentCondition)
class EquipmentConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(EquipmentStatus)
class EquipmentStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

