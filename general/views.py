from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404
from service_requests.models import ServiceRequest, RequestStatus, Repair
from user_management.models import User
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import check_password
from django.contrib import messages 

# Create your views here.
def home(request):
    
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

    return render(request, 'general/home.html', context)


# เข้าสู่ระบบ
def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not username or not password:
            messages.warning(request, 'กรุณากรอกชื่อผู้ใช้และรหัสผ่าน')
            return redirect('home')

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['name'] = user.name
                request.session['role'] = user.role  # เก็บ role ใน session
                request.session.set_expiry(3600)  # หมดอายุใน 1 ชั่วโมง
                messages.success(request, "เข้าสู่ระบบสำเร็จ")

                return redirect("staff_dashboard")

            else:
                messages.error(request, "รหัสผ่านไม่ถูกต้อง")
        except User.DoesNotExist:
            messages.error(request, "ชื่อผู้ใช้งานไม่ถูกต้อง")

        return redirect("home") 

    return render(request, "general/home.html") 


def logout_view(request):
    request.session.flush()  # เคลียร์ข้อมูลใน session ทั้งหมด
    messages.success(request, "ออกจากระบบสำเร็จ")
    return redirect("home")
