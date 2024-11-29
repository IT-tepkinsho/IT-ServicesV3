from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from user_management.models import User
from .models import (CameraCCTV, Equipment, Computer, Keyboard, Monitor, Mouse, Network, Printer, Scanner, 
                     Server, Ups, GroupProgram, Software)
from .forms import (CameraCCTVForm, EquipmentForm, ComputerForm, MonitorForm, MouseForm, KeyboardForm, NetworkForm, 
                    PrinterForm, ScannerForm, ServerForm, SoftwareForm, ProgramForm, UpsForm)
from django.http import JsonResponse

# View สำหรับแสดงรายการ Equipment
def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment_management/equipment_list.html', {'equipments': equipments})

# View สำหรับเพิ่ม Equipment
def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'equipment_management/equipment_form.html', {'form': form})

# View สำหรับแก้ไข Equipment
def equipment_update(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'equipment_management/equipment_form.html', {'form': form})

# View สำหรับลบ Equipment
def equipment_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# Views สำหรับแสดงรายการ Computer
def computer_list(request):
    computers = Computer.objects.all()
    return render(request, 'equipment_management/computer_list.html', {'computers': computers})

# view สำหรับเพิ่ม Computer
def computer_create(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('owner'))  # ตรวจสอบว่าได้ค่า owner มาหรือไม่
            form.save()
            return redirect('computer_list')
    else:
        form = ComputerForm()
    return render(request, 'equipment_management/computer_form.html', {'form': form})

# view สำหรับแก้ไข Computer
def computer_update(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    if request.method == 'POST':
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            print(form.cleaned_data.get('owner'))  # ตรวจสอบว่าได้ค่า owner มาหรือไม่
            form.save()
            return redirect('computer_list')
    else:
        form = ComputerForm(instance=computer)
    return render(request, 'equipment_management/computer_form.html', {'form': form})

# view สำหรับลบ Computer
def computer_delete(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    if request.method == 'POST':
        computer.delete()
        # ส่งข้อความแจ้งเตือนเมื่อการลบสำเร็จ
        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})
     # หากลบไม่สำเร็จ
    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

#ดึงข้อมูล monitor
def get_monitor_details(request, monitor_id):
    try:
        monitor = Monitor.objects.get(id=monitor_id)
        print(monitor.model) 
        return JsonResponse({'model': monitor.model})
    except Monitor.DoesNotExist:
        print(f"Monitor with ID {monitor_id} does not exist")
        return JsonResponse({'model': ''}, status=404)

#ดึงข้อมูล mouse
def get_mouse_details(request, mouse_id):
    try:
        mouse = Mouse.objects.get(id=mouse_id)
        print(mouse.brand)
        return JsonResponse({'brand': mouse.brand})
    except Mouse.DoesNotExist:
        print(f"Mouse with ID {mouse_id} does not exist")
        return JsonResponse({'brand': ''}, status=404)
    
#ดึงข้อมูล keyboard
def get_keyboard_details(request, keyboard_id):
    try:
        keyboard = Keyboard.objects.get(id=keyboard_id)
        print(keyboard.brand)
        return JsonResponse({'brand': keyboard.brand})
    except Keyboard.DoesNotExist:
        print(f"Keyboard with ID {keyboard_id} does not exist")
        return JsonResponse({'brand': ''}, status=404)
    
#ดึงข้อมูล printer
def get_printer_details(request, printer_id):
    try:
        printer = Printer.objects.get(id=printer_id)
        print(printer.model)
        return JsonResponse({'model': printer.model})
    except Printer.DoesNotExist:
        print(f"Printer with ID {printer_id} does not exist")
        return JsonResponse({'model': ''}, status=404)
    
#ดึงข้อมูล Scanner
def get_scanner_details(request, scanner_id):
    try:
        scanner = Scanner.objects.get(id=scanner_id)
        print(scanner.model)
        return JsonResponse({'model': scanner.model})
    except Scanner.DoesNotExist:
        print(f"Scanner with ID {scanner_id} does not exist")
        return JsonResponse({'model': ''}, status=404)
    
#ดึงข้อมูล UPS
def get_ups_details(request, ups_id):
    try:
        ups = Ups.objects.get(id=ups_id)
        print(ups.model)
        return JsonResponse({'model': ups.model})
    except Ups.DoesNotExist:
        print(f"UPS with ID {ups_id} does not exist")
        return JsonResponse({'model': ''}, status=404)
    
#ดึงข้อมูล Software
def get_software_details(request, software_id):
    try:
        software = Software.objects.get(id=software_id)
        print(software.name)
        print(software.license_key)
        return JsonResponse({'name': software.name, 'license_key': software.license_key})
    except software.DoesNotExist:
        print(f"software with ID {software_id} does not exist")
        return JsonResponse({'name': '', 'license_key': ''}, status=404)
    
#ดึงข้อมูล User
def get_owner_details(request, owner_id):
    try:
        owner = User.objects.get(id=owner_id)
        print(owner.nameTH)
        print(owner.department.name)
        return JsonResponse({'name': owner.nameTH, 'department': owner.department.name})
    except owner.DoesNotExist:
        print(f"owner with ID {owner_id} does not exist")
        return JsonResponse({'name': '', 'department': ''}, status=404)

# view สำหรับแสดงรายการ Monitor
def monitor_list(request):
    monitors = Monitor.objects.all()
    return render(request, 'equipment_management/monitor_list.html', {'monitors': monitors})

# view สำหรับเพิ่ม Monitor
def monitor_create(request):
    if request.method == 'POST':
        form = MonitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitor_list')
    else:
        form = MonitorForm()
    return render(request, 'equipment_management/monitor_form.html', {'form': form})

# view สำหรับแก้ไข Monitor
def monitor_update(request, pk):
    monitor = get_object_or_404(Monitor, pk=pk)
    if request.method == 'POST':
        form = MonitorForm(request.POST, instance=monitor)
        if form.is_valid():
            form.save()
            return redirect('monitor_list')
    else:
        form = MonitorForm(instance=monitor)
    return render(request, 'equipment_management/monitor_form.html', {'form': form})

# view สำหรับลบ Monitor
def monitor_delete(request, pk):
    monitor = get_object_or_404(Monitor, pk=pk)
    if request.method == 'POST':
        monitor.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# view สำหรับแสดงรายการ Mouse
def mouse_list(request):
    mouses = Mouse.objects.all()
    return render(request, 'equipment_management/mouse_list.html', {'mouses': mouses})

# view สำหรับเพิ่ม Mouse
def mouse_create(request):
    if request.method == 'POST':
        form = MouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mouse_list')
    else:
        form = MouseForm()
    return render(request, 'equipment_management/mouse_form.html', {'form': form})

# view สำหรับแก้ไข Mouse
def mouse_update(request, pk):
    mouse = get_object_or_404(Mouse, pk=pk)
    if request.method == 'POST':
        form = MouseForm(request.POST, instance=mouse)
        if form.is_valid():
            form.save()
            return redirect('mouse_list')
    else:
        form = MouseForm(instance=mouse)
    return render(request, 'equipment_management/mouse_form.html', {'form': form})

# view สำหรับลบ Mouse
def mouse_delete(request, pk):
    mouse = get_object_or_404(Mouse, pk=pk)
    if request.method == 'POST':
        mouse.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# view สำหรับแสดงรายการ Keyboard
def keyboard_list(request):
    keyboards = Keyboard.objects.all()
    return render(request, 'equipment_management/keyboard_list.html', {'keyboards': keyboards})

# view สำหรับเพิ่ม Keyboard
def keyboard_create(request):
    if request.method == 'POST':
        form = KeyboardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('keyboard_list')
    else:
        form = KeyboardForm()
    return render(request, 'equipment_management/keyboard_form.html', {'form': form})

# view สำหรับแก้ไข Keyboard
def keyboard_update(request, pk):
    keyboard = get_object_or_404(Keyboard, pk=pk)
    if request.method == 'POST':
        form = KeyboardForm(request.POST, instance=keyboard)
        if form.is_valid():
            form.save()
            return redirect('keyboard_list')
    else:
        form = KeyboardForm(instance=keyboard)
    return render(request, 'equipment_management/keyboard_form.html', {'form': form})

# view สำหรับลบ Keyboard
def keyboard_delete(request, pk):
    keyboard = get_object_or_404(Keyboard, pk=pk)
    if request.method == 'POST':
        keyboard.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# view สำหรับแสดงรายการ Printer
def printer_list(request):
    printers = Printer.objects.all()
    return render(request, 'equipment_management/printer_list.html', {'printers': printers})

def printer_create(request):
    if request.method == 'POST':
        form = PrinterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('printer_list')
    else:
        form = PrinterForm()
    return render(request, 'equipment_management/printer_form.html', {'form': form})

def printer_update(request, pk):
    printer = get_object_or_404(Printer, pk=pk)
    if request.method == 'POST':
        form = PrinterForm(request.POST, instance=printer)
        if form.is_valid():
            form.save()
            return redirect('printer_list')
    else:
        form = PrinterForm(instance=printer)
    return render(request, 'equipment_management/printer_form.html', {'form': form})

def printer_delete(request, pk):
    printer = get_object_or_404(Printer, pk=pk)
    if request.method == 'POST':
        printer.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def scanner_list(request):
    scanners = Scanner.objects.all()
    return render(request, 'equipment_management/scanner_list.html', {'scanners': scanners})

def scanner_create(request):
    if request.method == 'POST':
        form = ScannerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scanner_list')
    else:
        form = ScannerForm()
    return render(request, 'equipment_management/scanner_form.html', {'form': form})

def scanner_update(request, pk):
    scanner = get_object_or_404(Scanner, pk=pk)
    if request.method == 'POST':
        form = ScannerForm(request.POST, instance=pk)
        if form.is_valid():
            form.save()
            return redirect('scanner_list')
    else:
        form = ScannerForm(instance=scanner)
    return render(request, 'equipment_management/scanner_form.html')

def scanner_delete(request, pk):
    scanner = get_object_or_404(Scanner, pk=pk)
    if request.method == 'POST':
        scanner.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def ups_list(request):
    upses = Ups.objects.all()
    return render(request, 'equipment_management/ups_list.html', {'upses': upses})

def ups_create(request):
    if request.method == 'POST':
        form = UpsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ups_list')
    else:
        form = UpsForm()
    return render(request, 'equipment_management/ups_form.html', {'form': form})

def ups_update(request, pk):
    ups = get_object_or_404(Ups, pk=pk)
    if request.method == 'POST':
        form = UpsForm(request.POST, instance=ups)
        if form.is_valid():
            form.save()
            return redirect('ups_list')
    else:
        form = UpsForm(instance=ups)
    return render(request, 'equipment_management/ups_form.html', {'form': form})

def ups_delete(request, pk):
    ups = get_object_or_404(Ups, pk=pk)
    if request.method == 'POST':
        ups.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def server_list(request):
    servers = Server.objects.all();
    return render(request, 'equipment_management/server_list.html', {'servers': servers})

def server_create(request):
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('server_list')
    else:
        form = ServerForm()
    return render(request, 'equipment_management/server_form.html', {'form': form})

def server_update(request, pk):
    server = get_object_or_404(Server, pk=pk)
    if request.method == 'POST':
        form = ServerForm(request.POST, instance=server)
        if form.is_valid():
            form.save()
            return redirect('server_list')
    else:
        form = ServerForm(instance=server)
    return render(request, 'equipment_management/server_form.html', {'form': form})

def server_delete(request, pk):
    server = get_object_or_404(Server, pk=pk)
    if request.method == 'POST':
        server.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def network_list(request):
    networks = Network.objects.all()
    return render(request, 'equipment_management/network_list.html', {'networks': networks})

def network_create(request):
    if request.method == 'POST':
        form = NetworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('network_list')
    else:
        form = NetworkForm()
    return render(request, 'equipment_management/network_form.html', {'form': form})

def network_update(request, pk):
    network = get_object_or_404(Network, pk=pk)
    if request.method == 'POST':
        form = NetworkForm(request.POST, instance=network)
        if form.is_valid():
            form.save()
            return redirect('network_list')
    else:
        form = NetworkForm(instance=network)
    return render(request, 'equipment_management/network_form.html', {'form': form})

def network_delete(request, pk):
    network = get_object_or_404(Network, pk=pk)
    if request.method == 'POST':
        network.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def camera_cctv_list(request):
    camera_cctvs = CameraCCTV.objects.all()
    return render(request, 'equipment_management/camera_cctv_list.html', {'camera_cctvs': camera_cctvs})

def camera_cctv_create(request):
    if request.method == 'POST':
        form = CameraCCTVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('camera_cctv_list')
    else:
        form = CameraCCTVForm()
    return render(request, 'equipment_management/camera_cctv_form.html', {'form': form})

def camera_cctv_update(request, pk):
    camera_cctv = get_object_or_404(CameraCCTV, pk=pk)
    if request.method == 'POST':
        form = CameraCCTVForm(request.POST, instance=camera_cctv)
        if form.is_valid():
            form.save()
            return redirect('camera_cctv_list')
    else:
        form = CameraCCTVForm(instance=camera_cctv)
    return render(request, 'equipment_management/camera_cctv_form.html', {'form': form})

def camera_cctv_delete(request, pk):
    camera_cctv = get_object_or_404(CameraCCTV, pk=pk)
    if request.method == 'POST':
        camera_cctv.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def camera_cctv_create(request):
    if request.method == 'POST':
        form = CameraCCTVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('camera_cctv_list')
    else:
        form = CameraCCTVForm()
    return render(request, 'equipment_management/camera_cctv_form.html', {'form': form})

def camera_cctv_update(request, pk):
    camera_cctv = get_object_or_404(CameraCCTV, pk=pk)
    if request.method == 'POST':
        form = CameraCCTVForm(request.POST, instance=camera_cctv)
        if form.is_valid():
            form.save()
            return redirect('camera_cctv_list')
    else:
        form = CameraCCTVForm(instance=camera_cctv)
    return render(request, 'equipment_management/camera_cctv_form.html', {'form': form})

def camera_cctv_delete(request, pk):
    camera_cctv = get_object_or_404(CameraCCTV, pk=pk)
    if request.method == 'POST':
        camera_cctv.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Software
def software_list(request):
    softwares = Software.objects.all()  # ดึงข้อมูล Software ทั้งหมด
    return render(request, 'equipment_management/software_list.html', {'softwares': softwares,})

def software_create(request):
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('software_list')
    else:
        form = SoftwareForm()
    return render(request, 'equipment_management/software_form.html', {'form': form})

def software_update(request, pk):
    software = get_object_or_404(Software, pk=pk)
    if request.method == 'POST':
        form = SoftwareForm(request.POST, instance=software)
        if form.is_valid():
            form.save()
            return redirect('software_list')
    else:
        form = SoftwareForm(instance=software)
    return render(request, 'equipment_management/software_form.html', {'form': form})

def software_delete(request, pk):
    software = get_object_or_404(Software, pk=pk)
    if request.method == 'POST':
        software.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
