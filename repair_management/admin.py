from django.contrib import admin
from .models import RepairType, RepairTopic, Vendor
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



@admin.register(RepairType)
class RepairTypeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(RepairTopic)
class RepairTopicAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'repair_type')
    search_fields = ('name', 'repair_type__name')
    list_filter = ('repair_type',) 


@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'vendor_code', 'vendor_name', 'vendor_phone', 'email')
    search_fields = ('vendor_code', 'vendor_name')