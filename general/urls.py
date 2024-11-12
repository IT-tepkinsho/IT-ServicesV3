from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ฟังก์ชัน home
    path('login/', views.custom_login, name='custom_login'),  
    path('logout/', views.logout_view, name='logout'),  # เพิ่ม URL สำหรับ logout
]