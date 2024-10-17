from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipment
from .forms import EquipmentForm

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment_management/equipment_list.html', {'equipments': equipments})

def equipment_add(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'equipment_management/equipment_form.html', {'form': form})

def equipment_edit(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'equipment_management/equipment_form.html', {'form': form})
