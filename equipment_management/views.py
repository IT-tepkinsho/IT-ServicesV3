from ast import Return
from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment, Computer, Keyboard, Monitor, Mouse, Printer, Scanner, Ups
from .forms import (EquipmentForm, ComputerForm, MonitorForm, MouseForm, KeyboardForm, PrinterForm, ScannerForm,
                        ServerForm, SoftwareForm, ProgramForm)
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
        return redirect('computer_list')
    return render(request, 'equipment_management/computer_confirm_delete.html', {'computer': computer})

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
    return redirect(request, 'equipment_management/monitor_form.html', {'form': form})

# view สำหรับลบ Monitor
def monitor_delete(request, pk):
    monitor = get_object_or_404(Monitor, pk=pk)
    if request.method == 'POST':
        monitor.delete()
        return redirect('monitor_list')
    return render(request, 'equipment_management/monitor_confirm_delete.html', {'monitor': monitor})

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
    mouse = get_object_or_404(Mouse, pk)
    if request.method == 'POST':
        mouse.delete()
        return redirect('mouse_list')
    return render(request, 'equipment_management/mouse_confirm_delete.html', {'mouse': mouse})

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
    keyboard = get_object_or_404(Keyboard, pk)
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
        return redirect('keyboard_list')
    return render(request, 'equipment_management/keyboard_confirm_delete.html', {'keyboard': keyboard})

# view สำหรับแสดงรายการ Printer
def printer_list(request):
    printers = Printer.objects.all()
    return render(request, 'equipment_management/printer_list.html', {'printers': printers})

def printer_create(request):
    if request.method == 'POST':
        form = PrinterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('printer')
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
        return redirect('printer_list')
    return render(request, 'equipment_management/printer_confirm_delete', {'printer': printer})

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
        return redirect('scanner_list')
    return render(request, 'equipment_manage')

def ups_list(request):
    upses = Ups.objects.all()
    return render(request, 'equipment_management/ups_list.html', {'upses': upses})
