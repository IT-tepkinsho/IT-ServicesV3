from django.contrib import admin
from .models import (CameraCCTV, EquipmentCondition, EquipmentGroup, EquipmentStatus, EquipmentType, Computer, Monitor, Mouse,
                      Keyboard, Network, Printer, Server, Software, GroupProgram, Equipment, Scanner, Ups)

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
    list_display = ('equipment_code', 'brand', 'model', 'connection_type', 'cost', 'owner','vendor', 'status', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Keyboard model
@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'equipment_code', 'brand', 'model', 'connection_type', 'cost', 'owner','vendor', 'status',  'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)
# 
# Register the Printer model
@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'brand', 'model', 'print_type', 'warranty', 'ip_address', 'cost', 'owner','vendor', 'status', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Scanner model
@admin.register(Scanner)
class ScannerAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'brand', 'model', 'warranty', 'cost', 'owner','vendor', 'status', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Server model
@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'spec', 'location', 'ip_address', 'status', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Ups model
@admin.register(Ups)
class UpsAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'brand', 'model', 'warranty', 'cost', 'owner','vendor', 'status', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('equipment_type',)

# Register the Software model
@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'version', 'license_key', 'cost', 'group_program', 'owner' )
    search_fields = ('equipment_code', 'name', 'version')
    list_filter = ('group_program',)

# Register the Program model
@admin.register(GroupProgram)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


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


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'cost', 'ip_address', 'location', 'status')
    search_fields = ('name', 'brand', 'model',)
    list_filter = ('status',)


@admin.register(CameraCCTV)
class CameraCCTVAdmin(admin.ModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'cost', 'ip_address', 'status')
    search_fields = ('name', 'brand', 'model',)
    list_filter = ('status',)
