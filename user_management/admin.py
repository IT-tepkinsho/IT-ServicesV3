from django.contrib import admin
from .models import Department, User
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import CSV

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

# ปรับแต่งการแสดงผลในหน้าแอดมินสำหรับ Department
@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')  # ฟิลด์ที่ต้องการให้แสดงในตารางรายการ
    search_fields = ('name',)  # เพิ่มช่องค้นหาสำหรับฟิลด์ name

# ปรับแต่งการแสดงผลในหน้าแอดมินสำหรับ User
@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    formats = [UTF8SIGCSV]
    list_display = ('id', 'nameTH', 'nameEN', 'department', 'phone_number', 'email', 'role', 'username', 'password')  # ฟิลด์ที่ต้องการให้แสดง
    search_fields = ('nameTH', 'nameEN', 'department', 'phone_number', 'email', 'role')  # เพิ่มช่องค้นหาสำหรับฟิลด์ user
    list_filter = ('role',)  # เพิ่มตัวกรองตามสิทธิ์การใช้งาน

