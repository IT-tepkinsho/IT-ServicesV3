from django.contrib import admin
from .models import Equipment   # นำเข้า model ที่คุณต้องการจัดการใน admin

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'equipment_type', 'serial_number', 'purchase_date', 'warranty_expiration', 'status'] # กำหนดคอลัมน์ที่จะโชว์ใน list view
    search_fields = ['name', 'status'] # เพิ่มฟิลด์สำหรับค้นหา


admin.site.register(Equipment, EquipmentAdmin)  # ลงทะเบียน model และ custom admin