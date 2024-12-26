from import_export.formats.base_formats import CSV
from import_export.admin import ExportMixin
from django.contrib import admin
from .models import  ClaimUpdate, RepairClaim, RepairUpdateLog, ServiceRequest, Repair, Claim, ActivityLog, ServiceRequestConfig, RequestStatus
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
    
@admin.register(ServiceRequest)
class ServiceRequestAdmin(ImportExportModelAdmin):
    formats = [UTF8SIGCSV]
    list_display = (
        'service_request_number',
        'repair_type', 
        'repair_title', 
        'user_name', 
        'user_department', 
        'user_contact', 
        'attached_file',
        'request_description',
        'request_date',
        'repair_status',
        'repair_by',
        'feedback_submitted',
        )
    
    search_fields = (
        'service_request_number',
        'repair_type', 
        'repair_title', 
        'user_name', 
        'user_department', 
        'user_contact', 
        'request_description', 
        'repair_by',
    )
    list_filter = ['repair_status', 'feedback_submitted']


@admin.register(Repair)
class RepairAdmin(ImportExportModelAdmin):
    list_display = ('request', 'repair_details', 'repair_date')
    search_fields = ('request__user_name',)

@admin.register(Claim)
class ClaimAdmin(ImportExportModelAdmin):
    list_display = ('repair', 'claim_status', 'claim_date')
    search_fields = ('repair__request__user_name',)

@admin.register(ActivityLog)
class ActivityLogAdmin(ImportExportModelAdmin):
    list_display = ('service_request', 'action_taken', 'timestamp')
    search_fields = ('service_request__user_name',)

@admin.register(ServiceRequestConfig)
class ServiceRequestConfigAdmin(ImportExportModelAdmin):
    list_display = ('id','base_year', 'last_number')
    search_fields = ('base_year', 'last_number')


@admin.register(RequestStatus)
class RequestStatusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(RepairUpdateLog)
class RepairUpdateLogAdmin(ImportExportModelAdmin):
    list_display = ('id', 'service_request', 'update_datetime', 'total_repair_time', 'details')
    search_fields = ['service_request']

@admin.register(RepairClaim)
class RepairClaimAdmin(ImportExportModelAdmin):
    list_display = ('claim_number', 'service_request', 'equipment', 'company', 'claim_date', 'purpose_of_out', 'claim_status')
    search_fields = ('claim_number', 'company', 'equipment')
    list_filter = ['claim_status']

@admin.register(ClaimUpdate)
class ClaimUpdateAdmin(ImportExportModelAdmin):
    list_display = ('claim', 'update_date', 'details', 'status')
    list_filter = ['status']