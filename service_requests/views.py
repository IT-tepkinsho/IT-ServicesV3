from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from repair_management.models import RepairType, RepairTopic 
from user_management.models import User, Department
from .models import RepairClaim, ServiceRequest, Repair, Claim, ClaimUpdate, RequestStatus, RepairUpdateLog
from .forms import ServiceRequestForm, RepairForm, ClaimForm, ClaimUpdateForm, CompleteWorkForm, RepairDetailForm
from django.http import JsonResponse
import json
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.db.models import Count


# แสดงรายการ Service Requests List
def service_request_list(request):
    requests = ServiceRequest.objects.all()
    # ดึงข้อมูลจากโมเดล
    repair_types = RepairType.objects.all()
    departments = Department.objects.all()
    repair_statuses = RequestStatus.objects.all()

    context = {
        'requests': requests,
        'repair_types': repair_types,
        'departments': departments,
        'repair_statuses': repair_statuses,
    }

    return render(request, 'service_requests/service_request_list.html', context)


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

    service_request = get_object_or_404(ServiceRequest, pk=service_request_id)
    
    # ดึงข้อมูล repair ที่เชื่อมโยงกับ service request
    repairs = RepairUpdateLog.objects.filter(service_request=service_request)

    context = {
        'service_request': service_request,
        'repairs': repairs,
    }
    
    return render(request, 'service_requests/service_request_detail.html', context)

#ยกเลิกใบแจ้งซ่อม
def cancel_service_request(request, pk):
    # Get the service request by primary key (pk)
    service_request = get_object_or_404(ServiceRequest, pk=pk)

    # Get the 'canceled' status from RequestStatus
    canceled_status = get_object_or_404(RequestStatus, name='canceled') 

    # Update the repair_status to 'canceled'
    service_request.repair_status = canceled_status
    service_request.save()

    # Redirect back to the service request detail page
    return redirect(reverse('service_request_detail', args=[pk]))

# ดูรายละเอียดใบแจ้งซ่อม Staff
def service_request_job_detail(request, service_request_id):
    # ดึงข้อมูล service request ตาม id
    service_request = get_object_or_404(ServiceRequest, pk=service_request_id)
    
    # ดึงข้อมูล repair ที่เชื่อมโยงกับ service request
    # repairs = Repair.objects.filter(request=service_request)
    # request_statuses = RequestStatus.objects.filter(name__in=['pending' ,'in_progress', 'canceled'])

    repairs = RepairUpdateLog.objects.filter(service_request=service_request)

    if service_request.repair_status.name == 'pending':
        request_statuses = RequestStatus.objects.filter(name__in=['pending', 'in_progress', 'canceled'])
    elif service_request.repair_status.name == 'in_progress':
        request_statuses = RequestStatus.objects.filter(name__in=['in_progress', 'canceled'])
    else:
        request_statuses = []
    
    context = {
        'service_request': service_request,
        'repairs': repairs,
        'request_statuses': request_statuses,
    }
    
    return render(request, 'service_requests/service_request_job_detail.html', context)


def update_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        service_request_id = data.get('service_request_id')
        status_id = data.get('status')

        try:
            service_request = ServiceRequest.objects.get(id=service_request_id)
            status = RequestStatus.objects.get(id=status_id)
            
            # สถานะเป็น 'in_progress', ให้บันทึกวันที่เวลาใน date_receive
            if status.name == 'in_progress' and service_request.date_received is None:
                service_request.date_received = timezone.now()  # บันทึกเวลาปัจจุบัน

            service_request.repair_status = status
            service_request.save()

            return JsonResponse({'success': True})
        except ServiceRequest.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Service request not found'})
        except RequestStatus.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Status not found'})
        
@csrf_exempt
def update_repair_details(request):
    if request.method == 'POST':
        try:
            # อ่านข้อมูลจาก request.body
            data = json.loads(request.body)
            service_request_id = data.get('service_request_id')
            details = data.get('repair_details')

            # ตรวจสอบว่ามี service_request_id ในฐานข้อมูล
            service_request = ServiceRequest.objects.get(id=service_request_id)

            # สร้าง RepairUpdateLog
            RepairUpdateLog.objects.create(
                service_request=service_request,
                details=details
            )

            messages.success(request, 'บันทึกรายละเอียดการซ่อมสำเร็จ !')
            return JsonResponse({'success': True, 'redirect': True})

        except ServiceRequest.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Service request not found'}, status=404)

        except ValueError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data'}, status=400)

        except Exception as e:
            print(f"Error: {str(e)}")
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def update_claim_details(request):
    if request.method == 'POST':
        try:
           
            data = json.loads(request.body)
            claim_id = data.get('claim_id')
            details = data.get('details')
            update_date = data.get('update_date')
            status = data.get('status')

            claim = RepairClaim.objects.get(id=claim_id)

            ClaimUpdate.objects.create(
                claim=claim,
                details=details,
                update_date=update_date,
                status=status
            )

            # อัปเดตสถานะใน RepairClaim
            claim.claim_status = status
            claim.save()

            messages.success(request, 'บันทึกรายละเอียดการซ่อมสำเร็จ !')
            return JsonResponse({'success': True, 'redirect': True})

        except RepairClaim.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Claim not found'}, status=404)

        except ValueError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data'}, status=400)

        except Exception as e:
            print(f"Error: {str(e)}")
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

def complete_claim(request, pk):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            method_of_repair = data.get('method_of_repair', '')
            cost = data.get('cost', 0)
            operator = data.get('operator', '')

            # Get the RepairClaim object
            claim = get_object_or_404(RepairClaim, pk=pk)
            service_request = claim.service_request

            # Update the ServiceRequest object
            if service_request:
                service_request.method_of_repair = method_of_repair
                service_request.cost = cost
                service_request.operator = operator
                service_request.date_completed = timezone.now()

                # Calculate total repair time
                # if service_request.date_received:
                #     repair_time = service_request.date_completed - service_request.date_received
                #     service_request.total_repair_time = str(repair_time)

                # Update status to completed
                completed_status = RequestStatus.objects.get(name='completed')
                service_request.repair_status = completed_status

                service_request.save()

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

# ดึงประเภทการแจ้งซ่อม
def get_repair_topics(request):
    repair_type_id = request.GET.get('repair_type_id')
    print(f"Received repair_type_id: {repair_type_id}")  
    if repair_type_id:
        repair_topics = RepairTopic.objects.filter(repair_type_id=repair_type_id)
        print(f"Found topics: {repair_topics}")  
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

    return render(request, 'service_requests/service_request_list.html', {'repair_requests': repair_requests})


# ดึงข้อมูลผู้ใช้
def get_user_details(request):
    user_id = request.GET.get('user_id')
    user = get_object_or_404(User, id=user_id)

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


# สร้าง Claim ใหม่
def create_claim(request):
    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Claim has been created successfully!')
            return redirect('claim_list')  
    else:
        form = ClaimForm()
    return render(request, 'service_requests/external_repair_form.html', {'form': form})

# แสดงรายการ Claim ทั้งหมด
def claim_list(request):
    claims = RepairClaim.objects.all()
    return render(request, 'service_requests/tracking_claim.html', {'claims': claims})

# อัพเดต Claim
def update_claim(request, pk):
    claim = get_object_or_404(RepairClaim, pk=pk)
    updates = claim.updates.all()  # ใช้ related_name="updates" เพื่อเข้าถึงข้อมูล ClaimUpdate

    operator = request.session.get('name', '') 

    context = {
        'claim': claim,
        'updates': updates,
        'operator': operator,
    }

    return render(request, 'service_requests/external_repair_detail.html', context)

# ลบ Claim
def delete_claim(request, pk):
    claim = get_object_or_404(RepairClaim, pk=pk)
    if request.method == 'POST':
        claim.delete()
        messages.success(request, 'Claim has been deleted successfully!')
        return JsonResponse({'success': True})
    messages.error(request, 'Failed to delete claim.')
    return JsonResponse({'success': False})

def claim_tracking(request, claim_id):
    claim = get_object_or_404(RepairClaim, pk=claim_id)
    updates = claim.updates.all()  # Assuming related updates
    return render(request, 'service_requests/external_repair_tracking.html', {'claim': claim, 'updates': updates})


# Form IT_Repair
def it_repair_form(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)

    # ดึงค่าจาก session
    repair_by = request.session.get('repair_by', None)

    if request.method == 'POST':
        form = RepairDetailForm(request.POST, instance=service_request) 
        if form.is_valid():
            # อัปเดตข้อมูลเพิ่มเติม
            form.instance.operator = request.session.get('name', '')
            form.instance.date_completed = timezone.now() 

            # คำนวณ total_repair_time
            if form.instance.date_received and form.instance.date_completed:
                form.instance.total_repair_time = form.instance.date_completed - form.instance.date_received
            
            # เปลี่ยนสถานะเป็น complete
            try:
                complete_status = RequestStatus.objects.get(name='completed')
                form.instance.repair_status = complete_status
            except RequestStatus.DoesNotExist:
                raise ValueError("RequestStatus 'completed' not found.")

            # บันทึกข้อมูลใน ServiceRequest
            form.save()

            return redirect('service_request_job', service_request_id=service_request.id)
    else:
        initial_data = {
            'operator': request.session.get('name', ''),
            'equipment': service_request.equipment,
            'repair_by': service_request.repair_by,
        }

        form = RepairDetailForm(instance=service_request, initial=initial_data)
    
    return render(request, 'service_requests/it_repair_form.html', {'form': form, 'service_request': service_request})

def external_repair_form(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)

    if request.method == 'POST':
        form = ClaimForm(request.POST, service_request_instance=service_request)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.service_request = service_request  
            claim.save()
            return redirect('service_request_job', service_request_id=request_id)  
    else:
        form = ClaimForm(service_request_instance=service_request)

    return render(request, 'service_requests/external_repair_form.html', {'form': form, 'service_request': service_request})


def new_device_form(request):
    return render(request, 'service_requests/new_device_form.html')


def repair_detail_view(request, service_request_id):
    service_request = get_object_or_404(ServiceRequest, id=service_request_id)
    if request.method == "POST":
        form = RepairDetailForm(request.POST)
        if form.is_valid():
            repair_detail = form.save(commit=False)
            repair_detail.service_request = service_request
            repair_detail.save()
            return redirect('service_request_detail', id=service_request.id)
    else:
        # Pre-fill some fields if needed
        form = RepairDetailForm(initial={
            'equipment': service_request.equipment_code,
            'operator': request.session.get('name')
        })
    
    return render(request, 'service_requests/service_request_detail.html', {
        'form': form,
        'service_request': service_request
    })


#Table Services Request
def ticket_request(request):

    pending_requests = ServiceRequest.objects.filter(repair_status__name='pending')
    print(pending_requests) 

    in_progress_requests = ServiceRequest.objects.filter(repair_status__name='in_progress').prefetch_related('repair_updates')  # Prefetch related updates
    print(in_progress_requests) 

    completed_requests = ServiceRequest.objects.filter(repair_status__name='completed')
    print(completed_requests)

    canceled_requests = ServiceRequest.objects.filter(repair_status__name='canceled')
    print(canceled_requests)

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
    }

    return render(request, 'service_requests/ticket_request.html', context)

@csrf_exempt
def update_repair_by(request, request_id):
    if request.method == 'POST':

        data = json.loads(request.body)
        repair_by = data.get('repair_by')

        service_request = get_object_or_404(ServiceRequest, id=request_id)

        if repair_by:
            service_request.repair_by = repair_by
            service_request.save()

            return JsonResponse({'success': True})

        return JsonResponse({'success': False, 'error': 'Invalid data'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

# ประเมินความพึงพอใจ
class ServiceFeedbackView(View):
    template_name = 'service_requests/service_feedback.html'

    def get(self, request, pk):
        service_request = get_object_or_404(ServiceRequest, pk=pk)
        
        # ถ้าผู้ใช้เคยให้คะแนนแล้ว แสดงข้อความขอบคุณ
        if service_request.satisfaction_score is not None:
            return render(request, self.template_name, {
                'service_request': service_request,
                'feedback_given': True,  # แจ้งว่าให้คะแนนแล้ว
            })
        
        return render(request, self.template_name, {'service_request': service_request})

    def post(self, request, pk):
        service_request = get_object_or_404(ServiceRequest, pk=pk)

        # ตรวจสอบว่าผู้ใช้เคยให้คะแนนแล้วหรือยัง
        if service_request.satisfaction_score is not None:
            return render(request, self.template_name, {
                'service_request': service_request,
                'feedback_given': True,  # แจ้งว่าให้คะแนนแล้ว
                'message': 'คุณได้ให้คะแนนไปแล้ว',  # ข้อความเมื่อให้คะแนนซ้ำ
            })

        score = request.POST.get('satisfaction_score')
        comment = request.POST.get('feedback_comment')

        # บันทึกคะแนนและความคิดเห็น
        service_request.satisfaction_score = score
        service_request.feedback_comment = comment
        service_request.feedback_submitted = True  # บันทึกว่าผู้ใช้ประเมินแล้ว
        service_request.save()

        return render(request, self.template_name, {
            'service_request': service_request,
            'success': True  # แจ้งว่าให้คะแนนสำเร็จ
        })
    
# Chart ประเมินความพอใจ
def satisfaction_chart_view(request):
    # นับจำนวนคะแนนแต่ละระดับ
    satisfaction_data = (
        ServiceRequest.objects.values('satisfaction_score')
        .annotate(count=Count('satisfaction_score'))
        .order_by('satisfaction_score')
    )

    # แปลงข้อมูลให้อยู่ในรูปแบบที่ ECharts ใช้ได้
    chart_data = [
        {
            'value': data['count'],
            'name': {
                5: 'พอใจมากที่สุด',
                4: 'พอใจมาก',
                3: 'พอใจปานกลาง',
                2: 'พอใจน้อย',
                1: 'พอใจน้อยที่สุด'
            }.get(data['satisfaction_score'], 'ไม่มีข้อมูล')
        }
        for data in satisfaction_data
    ]

    return render(request, 'general/home.html', {'chart_data': chart_data})