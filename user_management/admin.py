from django.contrib import admin
from .models import Department, User

# ปรับแต่งการแสดงผลในหน้าแอดมินสำหรับ Department
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # ฟิลด์ที่ต้องการให้แสดงในตารางรายการ
    search_fields = ('name',)  # เพิ่มช่องค้นหาสำหรับฟิลด์ name

# ปรับแต่งการแสดงผลในหน้าแอดมินสำหรับ User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameTH', 'nameEN', 'department', 'phone_number', 'email', 'role', 'username', 'password')  # ฟิลด์ที่ต้องการให้แสดง
    search_fields = ('nameTH', 'nameEN', 'department', 'phone_number', 'email', 'role')  # เพิ่มช่องค้นหาสำหรับฟิลด์ user
    list_filter = ('role',)  # เพิ่มตัวกรองตามสิทธิ์การใช้งาน

