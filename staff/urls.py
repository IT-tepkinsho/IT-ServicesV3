# staff/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='staff_dashboard'),  # กำหนด URL name เป็น staff_dashboard
]
