from django.db import models
from django.contrib.auth.hashers import make_password

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User'),
    ]

    nameEN = models.CharField(max_length=100, verbose_name='ชื่ออังกฤษ')
    nameTH = models.CharField(max_length=100, verbose_name='ชื่อไทย')
    department = models.ForeignKey(Department, related_name='dept', on_delete=models.CASCADE, verbose_name='ฝ่าย')
    phone_number = models.CharField(max_length=15, verbose_name='เบอร์โต๊ะ')
    email = models.EmailField(max_length=254, verbose_name='อีเมล')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, verbose_name='ระดับผู้ใช้งาน')
    name = models.CharField(max_length=50, null=True, verbose_name='ชื่อกลาง')
    username = models.CharField(max_length=150, unique=True, verbose_name='ชื่อผู้ใช้งาน')
    password = models.CharField(max_length=128, verbose_name='รหัสผ่าน')  # เก็บรหัสผ่านแบบเข้ารหัส

    def __str__(self):
        return f"{self.nameTH}"

    def save(self, *args, **kwargs):
        # เช็คว่ารหัสผ่านนี้เข้ารหัสแล้วหรือยัง
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)