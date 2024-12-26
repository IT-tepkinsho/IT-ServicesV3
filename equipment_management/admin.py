from django.contrib import admin
from .models import (CameraCCTV, EquipmentCondition, EquipmentGroup, EquipmentStatus, EquipmentType, Computer, Monitor, Mouse,
                      Keyboard, Network, Printer, Server, Software, GroupProgram, Equipment, Scanner, SoftwareType, Ups, Tablet, Other)
from import_export.formats.base_formats import CSV
from import_export.admin import ImportExportModelAdmin

class UTF8SIGCSV(CSV):
    """
    Custom CSV format with UTF-8-sig encoding for proper Excel support.
    """
    def get_title(self):
        return "csv"

    def get_file_name(self, dataset):
        return "export.csv"

    def export_data(self, dataset, **kwargs):
        return super().export_data(dataset, **kwargs).encode("utf-8-sig")

# Register the EquipmentGroup model
@admin.register(EquipmentGroup)
class EquipmentGroupAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register the EquipmentType model
@admin.register(EquipmentType)
class EquipmentTypeAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'group')
    search_fields = ('name',)
    list_filter = ('group',)

# Register the Computer model
@admin.register(Computer)
class ComputerAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'spec', 'brand', 'vendor', 'owner', 'purchase_date', 'equipment_type', 'equipment_status')
    search_fields = ('equipment_code', 'brand', 'spec', 'vendor')
    list_filter = ('equipment_status',)
    list_per_page = 10

# Register the Monitor model
@admin.register(Monitor)
class MonitorAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'brand', 'model', 'serial_number', 'cost', 'warranty', 'vendor', 'owner', 'status', 'condition')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('status',)
    list_per_page = 10

# Register the Mouse model
@admin.register(Mouse)
class MouseAdmin(ImportExportModelAdmin): 
    list_display = ('equipment_code', 'brand', 'model', 'connection_type', 'cost', 'owner','vendor', 'status', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('status',)
    list_per_page = 10

# Register the Keyboard model
@admin.register(Keyboard)
class KeyboardAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'brand', 'model', 'connection_type', 'cost', 'owner','vendor', 'status',  'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('status',)
    list_per_page = 10
 
# Register the Printer model
@admin.register(Printer)
class PrinterAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'brand', 'model', 'print_type', 'warranty', 'ip_address', 'cost', 'owner','vendor', 'status', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('status',)
    list_per_page = 10

# Register the Scanner model
@admin.register(Scanner)
class ScannerAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'brand', 'model', 'warranty', 'cost', 'owner','vendor', 'status', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('status',)
    list_per_page = 10

# Register the Server model
@admin.register(Server)
class ServerAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'name', 'spec', 'location', 'ip_address', 'status', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('status',)
    list_per_page = 10

# Register the Ups model
@admin.register(Ups)
class UpsAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'brand', 'model', 'warranty', 'cost', 'owner','vendor', 'status', 'equipment_type')
    search_fields = ('equipment_code', 'brand', 'model')
    list_filter = ('status',)
    list_per_page = 10

# Register the Software model
@admin.register(Software)
class SoftwareAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'name', 'version', 'license_key', 'group_program', 'owner', 'status' )
    search_fields = ('equipment_code', 'name', 'version')
    list_filter = ('group_program', 'status')
    list_per_page = 10

# Register the Program model
@admin.register(GroupProgram)
class ProgramAdmin(ImportExportModelAdmin):
    list_display = ['name']
    search_fields = ['name']

# Register the software type model
@admin.register(SoftwareType)
class SoftwareTypeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'group')

# Register the Equipment model
@admin.register(Equipment)
class EquipmentAdmin(ImportExportModelAdmin):
    list_display = ('name', 'equipment_type', 'serial_number', 'purchase_date', 'warranty_expiration', 'status')
    search_fields = ('name', 'serial_number')
    list_filter = ('status',)

# Register the EquipmentCondition model
@admin.register(EquipmentCondition)
class EquipmentConditionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

# Register the EquipmentStatus model
@admin.register(EquipmentStatus)
class EquipmentStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

# Register the Network model
@admin.register(Network)
class NetworkAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'cost', 'ip_address', 'location', 'status')
    search_fields = ('name', 'brand', 'model')
    list_filter = ('status',)
    list_per_page = 10

# Register the CameraCCTV
@admin.register(CameraCCTV)
class CameraCCTVAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'cost', 'ip_address', 'status')
    search_fields = ('name', 'brand', 'model')
    list_filter = ('status',)
    list_per_page = 10

# Register the Tablet
@admin.register(Tablet)
class TabletAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'cost', 'status')
    search_fields = ('name', 'brand', 'model')
    list_filter = ('status',)
    list_per_page = 10

# Register the Other
@admin.register(Other)
class OtherAdmin(ImportExportModelAdmin):
    list_display = ('equipment_code', 'name', 'brand', 'model', 'cost', 'ip_address', 'status')
    search_fields = ('name', 'brand', 'model', 'ip_address')
    list_filter = ('status',)
    list_per_page = 10

