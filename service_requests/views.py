from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from repair_management.models import RepairType, RepairTopic 
from user_management.models import User, Department
from .models import ServiceRequest, Repair, RequestStatus
from .forms import ServiceRequestForm, RepairForm, ClaimForm, RequestForm
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import messages


# แสดงรายการ Service Requests List
def service_request_list(request):
    requests = ServiceRequest.objects.all()
    # ดึงข้อมูลจากโมเดล
    repair_types = RepairType.objects.all()
    departments = Department.objects.all()
    repair_statuses = RequestStatus.objects.all()

    return render(request, 'service_requests/service_request_list.html', {
        'requests': requests,
        'repair_types': repair_types,
        'departments': departments,
        'repair_statuses': repair_statuses,
    })

# แสดงรายการ Service Requests History
def service_request_history(request):
    historys = ServiceRequest.objects.all()
    return render(request, 'service_requests/service_request_history.html', {'history': historys})


# สร้าง Service Request ใหม่
def create_service_request(request):
    current_datetime = timezone.now()  # รูปแบบวันที่และเวลาตามที่ต้องการ
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)

        if form.is_valid():
            # ตั้งค่า request_date เมื่อสร้างใหม่
            form.instance.request_date = current_datetime  

            form.save() 
            # แจ้งเตือนเมื่อสร้าง Service Request สำเร็จ
            messages.success(request, "Service Request สร้างใบแจ้งซ่อมสำเร็จ !")

            return redirect('home')
        else:
            messages.error(request, 'สร้างใบแจ้งซ่อมไม่สำเร็จ กรุณาตรวจสอบข้อมูลอีกครั้ง!')
            # ถ้าข้อมูลไม่ถูกต้อง แสดงข้อผิดพลาดของฟอร์ม
            print(form.errors)  # แสดงข้อผิดพลาดใน console

    else:
        form = ServiceRequestForm()

    # ดึงข้อมูล RepairType ใช้ใน template
    repair_types = RepairType.objects.all()

    # ส่ง form และ error (ถ้ามี) กลับไปที่เทมเพลตเพื่อแสดงข้อผิดพลาดในหน้าเว็บ
    return render(request, 'service_requests/service_request_form.html', {
        'form': form,
        'current_datetime': current_datetime,
        'repair_types': repair_types,
    })


# ดูรายละเอียดใบแจ้งซ่อม
def service_request_detail(request, service_request_id):
    # ดึงข้อมูล service request ตาม id
    service_request = get_object_or_404(ServiceRequest, pk=service_request_id)
    
    # ดึงข้อมูล repair ที่เชื่อมโยงกับ service request
    repairs = Repair.objects.filter(request=service_request)
    
    context = {
        'service_request': service_request,
        'repairs': repairs,
    }
    
    return render(request, 'service_requests/service_request_detail.html', context)

# ยกเลิกใบแจ้งซ่อม
def cancel_service_request(request, pk):
    # Get the service request by primary key (pk)
    service_request = get_object_or_404(ServiceRequest, pk=pk)

    # Get the 'canceled' status from RequestStatus
    canceled_status = get_object_or_404(RequestStatus, name='canceled')  # สมมุติว่า name เป็นฟิลด์ที่เก็บชื่อสถานะ

    # Update the repair_status to 'canceled'
    service_request.repair_status = canceled_status
    service_request.save()

    # Redirect back to the service request detail page
    return redirect(reverse('service_request_detail', args=[pk]))

# ดึงประเภทการแจ้งซ่อม
def get_repair_topics(request):
    repair_type_id = request.GET.get('repair_type_id')
    print(f"Received repair_type_id: {repair_type_id}")  # Debugging
    if repair_type_id:
        repair_topics = RepairTopic.objects.filter(repair_type_id=repair_type_id)
        print(f"Found topics: {repair_topics}")  # Debugging
        repair_topics_data = [{"id": topic.id, "name": topic.name} for topic in repair_topics]
        return JsonResponse(repair_topics_data, safe=False)
    return JsonResponse([], safe=False)


# ดึงประวัติการแจ้งซ่อมจากการค้นหา
def get_repair_history(request):
    query_owner = request.GET.get('owner_name', '') 
    query_equipment_code = request.GET.get('equipment_code', '')

    service_requests = ServiceRequest.objects.all()

    if query_owner:
        service_requests = service_requests.filter(user_name__username__icontains=query_owner)  

    if query_equipment_code:
        service_requests = service_requests.filter(equipment__icontains=query_equipment_code) 

    context = {
        'service_requests': service_requests,  # ส่งผลลัพธ์ไปยัง template
    }
    return render(request, 'service_requests/service_request_history.html', context)


# ดึงรายการแจ้งซ่อม จากการค้นหา
def get_repair_list(request):
    # ดึงค่าจาก GET request
    repair_type = request.GET.get('repair_type', '')
    department = request.GET.get('department', '')
    repair_status = request.GET.get('repair_status', '')
    repair_user = request.GET.get('repair_user', '')
    repair_number = request.GET.get('repair_number', '')
    date_repair = request.GET.get('date_repair', '')
    date_complete = request.GET.get('date_complete', '')

    # เริ่มต้นด้วยการดึงข้อมูลบริการซ่อมทั้งหมด
    repair_requests = ServiceRequest.objects.all()

    # ใช้เงื่อนไขเพื่อกรองข้อมูลตามค่าที่ได้รับ
    if repair_type:
        repair_requests = repair_requests.filter(repair_type_id=repair_type)  # ใช้ repair_type_id
    if department:
        repair_requests = repair_requests.filter(user_department_id=department)  # ใช้ user_department_id
    if repair_status:
        repair_requests = repair_requests.filter(repair_status_id=repair_status)  # ใช้ repair_status_id
    if repair_user:
        repair_requests = repair_requests.filter(user_name__username__icontains=repair_user)
    if repair_number:
        repair_requests = repair_requests.filter(service_request_number__icontains=repair_number)
    if date_repair:
        repair_requests = repair_requests.filter(date_received__date=date_repair)
    if date_complete:
        repair_requests = repair_requests.filter(date_completed__date=date_complete)

    # ส่งข้อมูลที่กรองแล้วไปยังเทมเพลต
    return render(request, 'service_requests/service_request_list.html', {'repair_requests': repair_requests})


# ดึงข้อมูลผู้ใช้
def get_user_details(request):
    user_id = request.GET.get('user_id')
    user = get_object_or_404(User, id=user_id)

    # ส่งข้อมูลที่ต้องการใน JSON format
    data = {
        'department': user.department.name if user.department else '',
        'contact': user.phone_number,
    }
    return JsonResponse(data)


# สร้าง Repair
def create_repair(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.request = service_request
            repair.save()
            return redirect('service_request_list')
    else:
        form = RepairForm()
    return render(request, 'service_requests/repair_form.html', {'form': form, 'service_request': service_request})


# สร้าง Claim
def create_claim(request, repair_id):
    repair = get_object_or_404(Repair, id=repair_id)
    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.repair = repair
            claim.save()
            return redirect('service_request_list')
    else:
        form = ClaimForm()
    return render(request, 'service_requests/claim_form.html', {'form': form, 'repair': repair})

