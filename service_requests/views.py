from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceRequest, Repair, Claim
from .forms import ServiceRequestForm, RepairForm, ClaimForm
from datetime import datetime
from repair_management.models import RepairType, RepairTopic  # นำเข้าโมเดลจากแอป repair_management
from django.http import JsonResponse

# แสดงรายการ Service Requests
def service_request_list(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'service_requests/service_request_list.html', {'requests': requests})

# สร้าง Service Request ใหม่
def create_service_request(request):
    current_datetime = datetime.now().strftime('%d.%m.%Y %H:%M')  # รูปแบบวันที่และเวลาตามที่ต้องการ
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)  # ต้องเพิ่ม request.FILES เพื่อรองรับการอัพโหลดไฟล์
        if form.is_valid():
            form.instance.request_date = datetime.now()  # ตั้งค่า request_date เมื่อสร้างใหม่
            form.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm()
    
        # ดึงข้อมูล RepairType สำหรับใช้ใน template
        repair_types = RepairType.objects.all()

    return render(request, 'service_requests/service_request_form.html', {
            'form': form,
            'current_datetime': current_datetime,
            'repair_types': repair_types,
    })


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


# def get_repair_topics(request):
#     repair_type_id = request.GET.get('repair_type_id')
#     if repair_type_id:
#         repair_topics = RepairTopic.objects.filter(repair_type_id=repair_type_id)  # กรองหัวข้อการซ่อมตามประเภทการซ่อม
#         repair_topics_data = [{"id": topic.id, "name": topic.name} for topic in repair_topics]
#         return JsonResponse(repair_topics_data, safe=False)
#     return JsonResponse([], safe=False)  # คืนค่าเป็น JSON ว่ามีหัวข้อการซ่อมใด ๆ

def get_repair_topics(request):
    repair_type_id = request.GET.get('repair_type_id')
    print(f"Received repair_type_id: {repair_type_id}")  # Debugging
    if repair_type_id:
        repair_topics = RepairTopic.objects.filter(repair_type_id=repair_type_id)
        print(f"Found topics: {repair_topics}")  # Debugging
        repair_topics_data = [{"id": topic.id, "name": topic.name} for topic in repair_topics]
        return JsonResponse(repair_topics_data, safe=False)
    return JsonResponse([], safe=False)
