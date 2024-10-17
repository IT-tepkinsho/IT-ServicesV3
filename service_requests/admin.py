from urllib import request
from django.contrib import admin
from .models import ServiceRequest, Repair, Claim, ActivityLog

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = (
        'repair_type', 
        'repair_title', 
        'user_name', 
        'user_department', 
        'user_contact', 
        'equipment', 
        'attached_file',
        'request_description',
        'request_date',
        'request_status',
        'repair_by')
    search_fields = (
        'repair_type', 
        'repair_title', 
        'user_name', 
        'user_department', 
        'user_contact', 
        'equipment__name',  # ถ้า Equipment มีฟิลด์ชื่อ 'name'
        'request_description', 
        'request_status', 
        'repair_by'
    )
    list_filter = ['request_status']


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('request', 'repair_date', 'repair_status')
    search_fields = ('request__user_name',)

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('repair', 'claim_status', 'claim_date')
    search_fields = ('repair__request__user_name',)

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'action_taken', 'timestamp')
    search_fields = ('service_request__user_name',)
