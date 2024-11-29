from urllib import request
from django.contrib import admin
from .models import  RepairUpdateLog, ServiceRequest, Repair, Claim, ActivityLog, ServiceRequestConfig, RequestStatus

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = (
        'service_request_number',
        'repair_type', 
        'repair_title', 
        'user_name', 
        'user_department', 
        'user_contact', 
        # 'equipment', 
        'attached_file',
        'request_description',
        'request_date',
        'repair_status',
        'repair_by',
        )
    
    search_fields = (
        'service_request_number',
        'repair_type', 
        'repair_title', 
        'user_name', 
        'user_department', 
        'user_contact', 
        # 'equipment__name',  # ถ้า Equipment มีฟิลด์ชื่อ 'name'
        'request_description', 
        'repair_by',
    )
    list_filter = ['repair_status']


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('request', 'repair_details', 'repair_date')
    search_fields = ('request__user_name',)

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('repair', 'claim_status', 'claim_date')
    search_fields = ('repair__request__user_name',)

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'action_taken', 'timestamp')
    search_fields = ('service_request__user_name',)

@admin.register(ServiceRequestConfig)
class ServiceRequestConfigAdmin(admin.ModelAdmin):
    list_display = ('id','base_year', 'last_number')
    search_fields = ('base_year', 'last_number')


@admin.register(RequestStatus)
class RequestStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(RepairUpdateLog)
class RepairUpdateLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_request', 'update_datetime', 'total_repair_time', 'details')
    search_fields = ['service_request']