from multiprocessing import context
from sys import monitoring
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from user_management.models import User
from .models import (CameraCCTV, Equipment, Computer, Keyboard, Monitor, Mouse, Network, Printer, Scanner, 
                     Server, Tablet, Ups, GroupProgram, Software, Other)
from .forms import (CameraCCTVForm, EquipmentForm, ComputerForm, MonitorForm, MouseForm, KeyboardForm, NetworkForm, 
                    PrinterForm, ScannerForm, ServerForm, SoftwareForm, ProgramForm, TabletForm, UpsForm, OtherForm)
from django.http import JsonResponse
from django.forms import modelformset_factory

# SoftwareFormSet
SoftwareFormSet = modelformset_factory(Software, form=SoftwareForm, extra=1)

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Equipment
def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment_management/equipment_list.html', {'equipments': equipments})

def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'equipment_management/equipment_form.html', {'form': form})

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

def equipment_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Computer
def computer_list(request):
    computers = Computer.objects.all()
    computer_count = computers.count()  

    available_count = computers.filter(equipment_status__name='กำลังใช้งาน').count()
    empty_count = computers.filter(equipment_status__name='ว่าง').count()
    claim_count = computers.filter(equipment_status__name='ส่งเคลม').count()
    donate_count = computers.filter(equipment_status__name='บริจาค').count()
    
    context = {
       'computers': computers,
       'computer_count': computer_count,
       'available_count': available_count,
       'empty_count': empty_count,
       'claim_count': claim_count,
       'donate_count': donate_count,
    }

    return render(request, 'equipment_management/computer_list.html', context)

def computer_create(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        form = ComputerForm(request.POST)
        if form.is_valid():
            computer = form.save(commit=False)
            computer.save()
            form.save_m2m()  # Save Many-to-Many fields like `software`
            messages.success(request, 'Computer saved successfully.')
            return redirect('computer_list')
    else:
        form = ComputerForm()
        print("Form errors:", form.errors)
    return render(request, 'equipment_management/computer_form.html', {'form': form})

def computer_update(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    
    if request.method == 'POST':
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Computer saved successfully.')
            return redirect('computer_list')
    else:
        form = ComputerForm(instance=computer)
    
    # ดึงข้อมูลซอฟต์แวร์ที่สัมพันธ์กับคอมพิวเตอร์นี้
    software_data = computer.software.all()  # ซอฟต์แวร์ทั้งหมดที่สัมพันธ์กับคอมพิวเตอร์นี้

    context = {
        'form': form,
        'software_data': software_data
    }
    return render(request, 'equipment_management/computer_update.html', context)

def computer_delete(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    if request.method == 'POST':
        computer.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

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
    except Software.DoesNotExist: 
        print(f"Software with ID {software_id} does not exist")
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

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Monitor
def monitor_list(request):
    monitors = Monitor.objects.all()
    monitor_count = monitors.count()

    available_count = monitors.filter(status__name='กำลังใช้งาน').count()
    empty_count = monitors.filter(status__name='ว่าง').count()
    claim_count = monitors.filter(status__name='ส่งเคลม').count()
    donate_count = monitors.filter(status__name='บริจาค').count()

    context = {
        'monitors': monitors,
        'monitor_count': monitor_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_count': donate_count,
    }

    return render(request, 'equipment_management/monitor_list.html', context)

def monitor_create(request):
    if request.method == 'POST':
        form = MonitorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Monitor saved successfully.')
            return redirect('monitor_list')
    else:
        form = MonitorForm()
    return render(request, 'equipment_management/monitor_form.html', {'form': form})

def monitor_update(request, pk):
    monitor = get_object_or_404(Monitor, pk=pk)
    if request.method == 'POST':
        form = MonitorForm(request.POST, instance=monitor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Monitor saved successfully.')
            return redirect('monitor_list')
    else:
        form = MonitorForm(instance=monitor)
    return render(request, 'equipment_management/monitor_form.html', {'form': form})

def monitor_delete(request, pk):
    monitor = get_object_or_404(Monitor, pk=pk)
    if request.method == 'POST':
        monitor.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Mouse
def mouse_list(request):
    mouses = Mouse.objects.all()
    mouse_count = mouses.count()

    available_count = mouses.filter(status__name='กำลังใช้งาน').count()
    empty_count = mouses.filter(status__name='ว่าง').count()
    claim_count = mouses.filter(status__name='ส่งเคลม').count()
    donate_count = mouses.filter(status__name='บริจาค').count()

    context = {
        'mouses': mouses,
        'mouse_count': mouse_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_count': donate_count
    }

    return render(request, 'equipment_management/mouse_list.html', context)

def mouse_create(request):
    if request.method == 'POST':
        form = MouseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mouse saved successfully.')
            return redirect('mouse_list')
    else:
        form = MouseForm()
    return render(request, 'equipment_management/mouse_form.html', {'form': form})

def mouse_update(request, pk):
    mouse = get_object_or_404(Mouse, pk=pk)
    if request.method == 'POST':
        form = MouseForm(request.POST, instance=mouse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mouse saved successfully.')
            return redirect('mouse_list')
    else:
        form = MouseForm(instance=mouse)
    return render(request, 'equipment_management/mouse_form.html', {'form': form})

def mouse_delete(request, pk):
    mouse = get_object_or_404(Mouse, pk=pk)
    if request.method == 'POST':
        mouse.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ keyboard
def keyboard_list(request):
    keyboards = Keyboard.objects.all()
    keyboard_count = keyboards.count()

    available_count = keyboards.filter(status__name='กำลังใช้งาน').count()
    empty_count = keyboards.filter(status__name='ว่าง').count()
    claim_count = keyboards.filter(status__name='ส่งเคลม').count()
    donate_count = keyboards.filter(status__name='บริจาค').count()

    context = {
        'keyboards': keyboards,
        'keyboard_count': keyboard_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_claim': donate_count
    }

    return render(request, 'equipment_management/keyboard_list.html', context)

def keyboard_create(request):
    if request.method == 'POST':
        form = KeyboardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Keyboard saved successfully.')
            return redirect('keyboard_list')
    else:
        form = KeyboardForm()
    return render(request, 'equipment_management/keyboard_form.html', {'form': form})

def keyboard_update(request, pk):
    keyboard = get_object_or_404(Keyboard, pk=pk)
    if request.method == 'POST':
        form = KeyboardForm(request.POST, instance=keyboard)
        if form.is_valid():
            form.save()
            messages.success(request, 'Keyboard saved successfully.')
            return redirect('keyboard_list')
    else:
        form = KeyboardForm(instance=keyboard)
    return render(request, 'equipment_management/keyboard_form.html', {'form': form})

def keyboard_delete(request, pk):
    keyboard = get_object_or_404(Keyboard, pk=pk)
    if request.method == 'POST':
        keyboard.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Printer
def printer_list(request):
    printers = Printer.objects.all()
    printer_count = printers.count()

    available_count = printers.filter(status__name='กำลังใช้งาน').count()
    empty_count = printers.filter(status__name='ว่าง').count()
    claim_count = printers.filter(status__name='ส่งเคลม').count()
    donate_count = printers.filter(status__name='บริจาค').count()

    context = {
        'printers': printers,
        'printer_count': printer_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_count': donate_count
    }

    return render(request, 'equipment_management/printer_list.html', context)

def printer_create(request):
    if request.method == 'POST':
        form = PrinterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Printer saved successfully.')
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
            messages.success(request, 'Printer saved successfully.')
            return redirect('printer_list')
    else:
        form = PrinterForm(instance=printer)
    return render(request, 'equipment_management/printer_form.html', {'form': form})

def printer_delete(request, pk):
    printer = get_object_or_404(Printer, pk=pk)
    if request.method == 'POST':
        printer.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Scanner
def scanner_list(request):
    scanners = Scanner.objects.all()
    scanner_count = scanners.count()

    available_count = scanners.filter(status__name='กำลังใช้งาน').count()
    empty_count = scanners.filter(status__name='ว่าง').count()
    claim_count = scanners.filter(status__name='ส่งเคลม').count()
    donate_count = scanners.filter(status__name='บริจาค').count()

    context = {
        'scanners': scanners,
        'scanner_count': scanner_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_count': donate_count
    }
    return render(request, 'equipment_management/scanner_list.html', context)

def scanner_create(request):
    if request.method == 'POST':
        form = ScannerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Scanner saved successfully.')
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
            messages.success(request, 'Scanner saved successfully.')
            return redirect('scanner_list')
    else:
        form = ScannerForm(instance=scanner)
    return render(request, 'equipment_management/scanner_form.html', {'form': form})

def scanner_delete(request, pk):
    scanner = get_object_or_404(Scanner, pk=pk)
    if request.method == 'POST':
        scanner.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ UPS
def ups_list(request):
    upses = Ups.objects.all()
    ups_count = upses.count()

    available_count = upses.filter(status__name='กำลังใช้งาน').count()
    empty_count = upses.filter(status__name='ว่าง').count()
    claim_count = upses.filter(status__name='ส่งเคลม').count()
    donate_count = upses.filter(status__name='บริจาค').count()

    context = {
        'upses': upses,
        'ups_count': ups_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_count': donate_count
    }
    return render(request, 'equipment_management/ups_list.html', context)

def ups_create(request):
    if request.method == 'POST':
        form = UpsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'UPS saved successfully.')
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
            messages.success(request, 'UPS saved successfully.')
            return redirect('ups_list')
    else:
        form = UpsForm(instance=ups)
    return render(request, 'equipment_management/ups_form.html', {'form': form})

def ups_delete(request, pk):
    ups = get_object_or_404(Ups, pk=pk)
    if request.method == 'POST':
        ups.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Server
def server_list(request):
    servers = Server.objects.all();
    server_count = servers.count()

    available_count = servers.filter(status__name='กำลังใช้งาน').count()
    empty_count = servers.filter(status__name='ว่าง').count()
    claim_count = servers.filter(status__name='ส่งเคลม').count()
    donate_count = servers.filter(status__name='บริจาค').count()

    context = {
        'servers': servers,
        'server_count': server_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_count': donate_count
    }
    return render(request, 'equipment_management/server_list.html', context)

def server_create(request):
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Server saved successfully.')
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
            messages.success(request, 'Server saved successfully.')
            return redirect('server_list')
    else:
        form = ServerForm(instance=server)
    return render(request, 'equipment_management/server_form.html', {'form': form})

def server_delete(request, pk):
    server = get_object_or_404(Server, pk=pk)
    if request.method == 'POST':
        server.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Network
def network_list(request):
    networks = Network.objects.all()
    network_count = networks.count()

    available_count = networks.filter(status__name='กำลังใช้งาน').count()
    empty_count = networks.filter(status__name='ว่าง').count()
    claim_count = networks.filter(status__name='ส่งเคลม').count()
    donate_count = networks.filter(status__name='บริจาค').count()

    context = {
        'networks': networks,
        'network_count': network_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_count': donate_count
    }

    return render(request, 'equipment_management/network_list.html', context)

def network_create(request):
    if request.method == 'POST':
        form = NetworkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Network saved successfully.')
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
            messages.success(request, 'Network saved successfully.')
            return redirect('network_list')
    else:
        form = NetworkForm(instance=network)
    return render(request, 'equipment_management/network_form.html', {'form': form})

def network_delete(request, pk):
    network = get_object_or_404(Network, pk=pk)
    if request.method == 'POST':
        network.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Camera CCTV
def camera_cctv_list(request):
    camera_cctvs = CameraCCTV.objects.all()
    camera_count = camera_cctvs.count()

    available_count = camera_cctvs.filter(status__name='กำลังใช้งาน').count()
    empty_count = camera_cctvs.filter(status__name='ว่าง').count()
    claim_count = camera_cctvs.filter(status__name='ส่งเคลม').count()
    donate_count = camera_cctvs.filter(status__name='บริจาค').count()

    context = {
        'camera_cctvs': camera_cctvs,
        'camera_count': camera_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_count': donate_count
    }

    return render(request, 'equipment_management/camera_cctv_list.html', context)


def camera_cctv_create(request):
    if request.method == 'POST':
        form = CameraCCTVForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Camera CCTV saved successfully.')
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
            messages.success(request, 'Camera CCTV saved successfully.')
            return redirect('camera_cctv_list')
    else:
        form = CameraCCTVForm(instance=camera_cctv)
    return render(request, 'equipment_management/camera_cctv_form.html', {'form': form})

def camera_cctv_delete(request, pk):
    camera_cctv = get_object_or_404(CameraCCTV, pk=pk)
    if request.method == 'POST':
        camera_cctv.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Software
def software_list(request):
    softwares = Software.objects.all()
    software_count = softwares.count()

    available_count = softwares.filter(status__name='กำลังใช้งาน').count()
    empty_count = softwares.filter(status__name='ว่าง').count()
    claim_count = softwares.filter(status__name='ส่งเคลม').count()
    donate_count = softwares.filter(status__name='บริจาค').count()

    context = {
        'softwares': softwares,
        'software_count': software_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_claim': donate_count
    }

    return render(request, 'equipment_management/software_list.html', context)

def software_create(request):
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Software saved successfully.')
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
            messages.success(request, 'Software saved successfully.')
            return redirect('software_list')
    else:
        form = SoftwareForm(instance=software)
    return render(request, 'equipment_management/software_form.html', {'form': form})

def software_delete(request, pk):
    software = get_object_or_404(Software, pk=pk)
    if request.method == 'POST':
        software.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Tablet
def tablet_list(request):
    tablets = Tablet.objects.all()
    tablet_count = tablets.count()

    available_count = tablets.filter(status__name='กำลังใช้งาน').count()
    empty_count = tablets.filter(status__name='ว่าง').count()
    claim_count = tablets.filter(status__name='ส่งเคลม').count()
    donate_count = tablets.filter(status__name='บริจาค').count()

    context = {
        'tablets': tablets,
        'tablet_count': tablet_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_claim': donate_count
    }
    return render(request, 'equipment_management/tablet_list.html', context)

def tablet_create(request):
    if request.method == 'POST':
        form = TabletForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tablet saved successfully.')
            return redirect('tablet_list')
    else:
        form = TabletForm()
    return render(request, 'equipment_management/tablet_form.html', {'form': form})

def tablet_update(request, pk):
    tablet = get_object_or_404(Tablet, pk=pk)
    if request.method == 'POST':
        form = TabletForm(request.POST, instance=tablet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tablet saved successfully.')
            return redirect('tablet_list')
    else:
        form = TabletForm(instance=tablet)
    return render(request, 'equipment_management/tablet_form.html', {'form': form})

def tablet_delete(request, pk):
    tablet = get_object_or_404(Tablet, pk=pk)
    if request.method == 'POST':
        tablet.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

# ฟังก์ชันสำหรับแสดงรายการทั้งหมดของ Other
def other_list(request):
    others = Other.objects.all()
    other_count = others.count()

    available_count = others.filter(status__name='กำลังใช้งาน').count()
    empty_count = others.filter(status__name='ว่าง').count()
    claim_count = others.filter(status__name='ส่งเคลม').count()
    donate_count = others.filter(status__name='บริจาค').count()

    context = {
        'others': others,
        'other_count': other_count,
        'available_count': available_count,
        'empty_count': empty_count,
        'claim_count': claim_count,
        'donate_count': donate_count
    }

    return render(request, 'equipment_management/other_list.html', context)

def other_create(request):
    if request.method == 'POST':
        form = OtherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipment saved successfully.')
            return redirect('other_list')
    else:
        form = OtherForm()
    return render(request, 'equipment_management/other_form.html', {'form': form})

def other_update(request, pk):
    other = get_object_or_404(Other, pk=pk)
    if request.method == 'POST':
        form = OtherForm(request.POST, instance=other)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipment saved successfully.')
            return redirect('other_list')
    else:
        form = OtherForm(instance=other)
    return render(request, 'equipment_management/other_form.html', {'form': form})

def other_delete(request, pk):
    other = get_object_or_404(Other, pk=pk)
    if request.method == 'POST':
        other.delete()

        messages.success(request, 'Equipment has been deleted successfully.')
        return JsonResponse({'success': True})

    messages.error(request, 'Failed to delete equipment.')
    return JsonResponse({'success': False})

