from django.contrib import admin
from .models import RepairType, RepairTopic

# ปรับแต่งการแสดงผลในหน้าแอดมินสำหรับ RepairType
@admin.register(RepairType)
class RepairTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # ฟิลด์ที่ต้องการให้แสดงในตารางรายการ
    search_fields = ('name',)  # เพิ่มช่องค้นหาสำหรับฟิลด์ name

# ปรับแต่งการแสดงผลในหน้าแอดมินสำหรับ RepairTopic
@admin.register(RepairTopic)
class RepairTopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'repair_type')  # ฟิลด์ที่ต้องการให้แสดง
    search_fields = ('name', 'repair_type__name')  # เพิ่มช่องค้นหาสำหรับฟิลด์ topic
    list_filter = ('repair_type',)  # เพิ่มตัวกรองตามประเภทการซ่อม

