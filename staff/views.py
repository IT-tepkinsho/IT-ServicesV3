# staff/views.py
from django.shortcuts import render, redirect
from user_management.models import User
from service_requests.models import ServiceRequest
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta

def dashboard(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            return render(request, "staff/index.html", {"user": user})
        except User.DoesNotExist:
            # กรณีที่ user_id ไม่มีในฐานข้อมูล ให้ลบ session และ redirect ไปหน้า login
            request.session.flush()
            messages.error(request, "ไม่พบข้อมูลผู้ใช้งานในระบบ")
            return redirect("custom_login")
    
    return redirect("custom_login")

def dashboard(request):
    # ดึงข้อมูลคำร้องบริการตามสถานะ
    pending_requests = ServiceRequest.objects.filter(repair_status__name='pending')
    print(pending_requests) 

    in_progress_requests = ServiceRequest.objects.filter(repair_status__name='in_progress')
    print(in_progress_requests) 

    completed_requests = ServiceRequest.objects.filter(repair_status__name='completed')
    print(completed_requests)

    canceled_requests = ServiceRequest.objects.filter(repair_status__name='canceled')
    print(canceled_requests)


    # คำนวณจำนวนใบแจ้งซ่อม
    new_requests_count = ServiceRequest.objects.filter(repair_status__name='pending').count()  # จำนวนใบแจ้งซ่อมใหม่
    in_progress_requests_count = in_progress_requests.count()  # จำนวนใบแจ้งซ่อมรอแก้ไข
    monthly_requests_count = ServiceRequest.objects.filter(request_date__gte=timezone.now() - timedelta(days=30)).count()  # จำนวนใบแจ้งซ่อมในเดือนนี้
    yearly_requests_count = ServiceRequest.objects.filter(request_date__gte=timezone.now() - timedelta(days=365)).count()  # จำนวนใบแจ้งซ่อมในปีนี้


    # นับจำนวนคำร้องในแต่ละสถานะ
    pending_count = pending_requests.count()
    in_progress_count = in_progress_requests.count()
    completed_count = completed_requests.count()
    canceled_count = canceled_requests.count()

    # สร้างตัวแปร context เพื่อส่งข้อมูลไปยัง template
    context = {
        'pending_requests': pending_requests,
        'in_progress_requests': in_progress_requests,
        'completed_requests': completed_requests,
        'canceled_requests': canceled_requests,
        'pending_count': pending_count,
        'in_progress_count': in_progress_count,
        'completed_count': completed_count,
        'canceled_count': canceled_count,
        'new_requests_count': new_requests_count,
        'in_progress_requests_count': in_progress_requests_count,
        'monthly_requests_count': monthly_requests_count,
        'yearly_requests_count': yearly_requests_count,
    }

    return render(request, 'staff/index.html', context)
