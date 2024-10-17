from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('IT', 'IT'),
        ('user', 'User'),
    ]

    nameEN = models.CharField(max_length=100, verbose_name='ชื่ออังกฤษ')
    nameTH = models.CharField(max_length=100, verbose_name='ชื่อไทย')
    department = models.CharField(max_length=100, verbose_name='แผนก')
    phone_number = models.CharField(max_length=15, verbose_name='เบอร์โต๊ะ')
    email = models.EmailField(max_length=254, verbose_name='อีเมล')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, verbose_name='ระดับผู้ใช้งาน')
    username = models.CharField(max_length=150, unique=True, verbose_name='ชื่อผู้ใช้งาน')
    password = models.CharField(max_length=128, verbose_name='รหัสผ่าน')  # อาจจะใช้การเข้ารหัสรหัสผ่านเพิ่มเติมด้วย

    def __str__(self):
        return self.namEN  # หรือใช้ nameTH หรือ username ตามที่ต้องการ
