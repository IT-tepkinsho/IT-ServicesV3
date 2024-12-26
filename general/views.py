from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404
from service_requests.models import ServiceRequest, RequestStatus, Repair
from user_management.models import User
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from django.contrib.auth.hashers import check_password
from django.contrib import messages 
import json
from django.db.models import Count, Sum, F, Case, When
from datetime import datetime

def home(request):
    # สร้าง dictionary สำหรับแปลงชื่อเดือนเป็นภาษาไทย
    MONTHS_TH = {
        'January': 'มกราคม',
        'February': 'กุมภาพันธ์',
        'March': 'มีนาคม',
        'April': 'เมษายน',
        'May': 'พฤษภาคม',
        'June': 'มิถุนายน',
        'July': 'กรกฎาคม',
        'August': 'สิงหาคม',
        'September': 'กันยายน',
        'October': 'ตุลาคม',
        'November': 'พฤศจิกายน',
        'December': 'ธันวาคม',
    }

    pending_requests = ServiceRequest.objects.filter(repair_status__name='pending')
    print(pending_requests) 

    in_progress_requests = ServiceRequest.objects.filter(repair_status__name='in_progress').prefetch_related('repair_updates')  # Prefetch related updates
    print(in_progress_requests) 

    completed_requests = ServiceRequest.objects.filter(repair_status__name='completed')
    print(completed_requests)

    canceled_requests = ServiceRequest.objects.filter(repair_status__name='canceled')
    print(canceled_requests)


    # วันที่เริ่มต้นของเดือนนี้
    today = timezone.now()
    start_of_month = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    # คำนวณวันที่เริ่มต้นของปีนี้
    start_of_year = today.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

    # คำนวณจำนวนใบแจ้งซ่อม
    new_requests_count = ServiceRequest.objects.filter(repair_status__name='pending').count()  # จำนวนใบแจ้งซ่อมใหม่
    in_progress_requests_count = in_progress_requests.count()  # จำนวนใบแจ้งซ่อมรอแก้ไข
    
    monthly_requests_count = ServiceRequest.objects.filter(
        request_date__gte=start_of_month, request_date__lte=today
    ).count()
    yearly_requests_count = ServiceRequest.objects.filter(
        request_date__gte=start_of_year, request_date__lte=today
    ).count()


    # ดึงชื่อเดือนในภาษาอังกฤษ
    month_name_en = today.strftime('%B') 
    
    # แปลงชื่อเดือนเป็นภาษาไทย
    month_name_th = MONTHS_TH.get(month_name_en, month_name_en) 


    # นับจำนวนคำร้องในแต่ละสถานะ
    pending_count = pending_requests.count()
    in_progress_count = in_progress_requests.count()
    completed_count = completed_requests.count()
    canceled_count = canceled_requests.count()

    # ดึงข้อมูลสถิติการแจ้งซ่อม
    repair_data = (
        ServiceRequest.objects.values('repair_type__name')
        .annotate(count=Count('repair_type'))
        .order_by('-count')
    )

    repair_chart_data = [{"name": item['repair_type__name'], "value": item['count']} for item in repair_data]
    
    # ดึงข้อมูลคะแนนความพึงพอใจ
    satisfaction_data = (
        ServiceRequest.objects.values('satisfaction_score')
        .annotate(count=Count('satisfaction_score'))
        .order_by('satisfaction_score')
    )

    # แปลงข้อมูลให้อยู่ในรูปแบบที่ใช้ในกราฟ
    chart_data = [
        {
            'value': data['count'],
            'name': {
                5: 'มากที่สุด',
                4: 'มาก',
                3: 'ปานกลาง',
                2: 'น้อย',
                1: 'น้อยที่สุด'
            }.get(data['satisfaction_score'], 'ไม่มีข้อมูล')
        }
        for data in satisfaction_data
    ]



    # ดึงข้อมูลการซ่อมจาก ServiceRequest โดยรวมข้อมูลตามประเภทการซ่อม

    # ดึงปีและเดือนจาก GET request (ถ้าไม่มีจะใช้ค่าปัจจุบัน)
    current_month = datetime.now().month
    current_year = datetime.now().year
    years = [year for year in range(current_year - 1, current_year + 10)]

    # ดึงค่าจาก request
    month = request.GET.get('month', None)  # รับค่าจากฟอร์ม
    year = request.GET.get('year', current_year)  # ค่าเริ่มต้นคือปีปัจจุบัน

    # กรองข้อมูลตามเดือนและปี
    repair_data = (
        ServiceRequest.objects
        .filter(request_date__year=year)  # กรองข้อมูลตามปี
    )

    if month:  # ถ้ามีการเลือกเดือน
        repair_data = repair_data.filter(request_date__month=month)

    repair_data = repair_data.values(
        "repair_type__name",
        "repair_title__name",
        "repair_by"
    ).annotate(
        total_requests=Count("id"),
        total_cost=Sum("cost"),
        it_count=Count(Case(When(repair_by='it_repair', then=1))),
        outsource_count=Count(Case(When(repair_by='external_repair', then=1))),
    )

    it_repair_types = ["อุปกรณ์ IT"]

    # คำนวณผลรวมทั้งหมด
    total_requests_all = 0
    total_cost_all = 0

    # จัดกลุ่มตาม repair_type
    summary_data = {}
    for data in repair_data:
        repair_type = data["repair_type__name"]
        repair_title = data["repair_title__name"]

        if repair_type not in summary_data:
            summary_data[repair_type] = {
                "subtopics": {},
                "total_requests": 0,
                "total_cost": 0,
                "it_count": 0,
                "outsource_count": 0,
            }

        # รวมข้อมูลตาม repair_title สำหรับทุกประเภท
        if repair_title not in summary_data[repair_type]["subtopics"]:
            summary_data[repair_type]["subtopics"][repair_title] = {
                "total_requests": 0,
                "total_cost": 0,
                "it_count": 0,
                "outsource_count": 0,
            }

        # เพิ่มข้อมูลที่เกี่ยวข้อง
        summary_data[repair_type]["subtopics"][repair_title]["total_requests"] += data["total_requests"]
        summary_data[repair_type]["subtopics"][repair_title]["total_cost"] += data["total_cost"] or 0
        summary_data[repair_type]["subtopics"][repair_title]["it_count"] += data["it_count"]
        summary_data[repair_type]["subtopics"][repair_title]["outsource_count"] += data["outsource_count"]

        # รวมข้อมูลรวมสำหรับ repair_type
        summary_data[repair_type]["total_requests"] += data["total_requests"]
        summary_data[repair_type]["total_cost"] += data["total_cost"] or 0
        summary_data[repair_type]["it_count"] += data["it_count"]
        summary_data[repair_type]["outsource_count"] += data["outsource_count"]

    # คำนวณผลรวมทั้งหมด (รวมทุก repair_type)
    total_requests_all = sum(data["total_requests"] for data in summary_data.values())
    total_cost_all = sum(data["total_cost"] for data in summary_data.values())

    # ส่ง context ไปยัง template
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
        'month_name': month_name_th,
        'yearly_requests_count': yearly_requests_count,
        'chart_data': json.dumps(chart_data),
        'repair_chart_data': json.dumps(repair_chart_data),
        'summary_data': summary_data,
        'repair_data': repair_data,
        'it_repair_types': it_repair_types,
        'total_requests_all': total_requests_all,
        'total_cost_all': total_cost_all,
        'current_year': current_year,
        'current_month': current_month,
        'years': years,
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
                request.session.set_expiry(28800)  # หมดอายุใน 1 ชั่วโมง
                messages.success(request, "เข้าสู่ระบบสำเร็จ")

                return redirect("ticket_request")

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
