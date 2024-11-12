from django.shortcuts import render, redirect, get_object_or_404
from .models import RepairType, RepairTopic, Vendor
from .forms import RepairTypeForm, RepairTopicForm, VendorForm

# แสดงรายการประเภทการซ่อม
def repair_type_list(request):
    repair_types = RepairType.objects.all()
    return render(request, 'repair_management/repair_type_list.html', {'repair_types': repair_types})

# สร้างประเภทการซ่อมใหม่
def create_repair_type(request):
    if request.method == 'POST':
        form = RepairTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repair_type_list')
    else:
        form = RepairTypeForm()
    return render(request, 'repair_management/repair_type_form.html', {'form': form})

# แก้ไขประเภทการซ่อม
def edit_repair_type(request, pk):
    repair_type = get_object_or_404(RepairType, pk=pk)
    if request.method == 'POST':
        form = RepairTypeForm(request.POST, instance=repair_type)
        if form.is_valid():
            form.save()
            return redirect('repair_type_list')
    else:
        form = RepairTypeForm(instance=repair_type)
    return render(request, 'repair_management/repair_type_form.html', {'form': form})

# ลบประเภทการซ่อม
def delete_repair_type(request, pk):
    repair_type = get_object_or_404(RepairType, pk=pk)
    repair_type.delete()
    return redirect('repair_type_list')

# แสดงรายการหัวข้อการซ่อม
def repair_topic_list(request):
    repair_topics = RepairTopic.objects.all()
    return render(request, 'repair_management/repair_topic_list.html', {'repair_topics': repair_topics})

# สร้างหัวข้อการซ่อม
def create_repair_topic(request):
    if request.method == 'POST':
        form = RepairTopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repair_topic_list')
    else:
        form = RepairTopicForm()
    return render(request, 'repair_management/repair_topic_form.html', {'form': form})


# แก้ไขหัวข้อการซ่อม
def edit_repair_topic(request, pk):
    repair_topic = get_object_or_404(RepairTopic, pk=pk)
    if request.method == 'POST':
        form = RepairTopicForm(request.POST, instance=repair_topic)
        if form.is_valid():
            form.save()
            return redirect('repair_topic_list')
    else:
            form = RepairTopicForm(instance=repair_topic)
    return render(request, 'repair_management/repair_topic_form.html', {'form': form})

# ลบหัวข้อการซ่อม
def delete_repair_topic(request, pk):
    repair_topic = get_object_or_404(RepairTopic, pk=pk)
    repair_topic.delete()
    return redirect('repair_topic_list')


def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'repair_management/vendor_list.html', {'vendors': vendors})

def create_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'repair_management/vendor_form.html', {'form': form})

def vendor_update(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
            form = VendorForm(instance=vendor)
    return render(request, 'repair_management/vendor_form.html', {'form': form})

def vendor_delete(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor_list')