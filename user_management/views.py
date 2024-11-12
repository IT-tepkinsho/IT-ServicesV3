from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Department
from .forms import DepartmentForm, UserForm
from django.contrib.auth.hashers import check_password
from django.contrib import messages 

#Department
def department_list(request):
    departments = Department.objects.all()  
    return render(request, 'user_management/department_list.html', {'departments': departments})

def create_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'user_management/department_form.html', {'form': form} )


def edit_department(request, pk):
    user = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=user)
    return render(request, 'user_management/department_form.html', {'form': form})


def delete_department(request, pk):
    user = get_object_or_404(Department, pk=pk)
    user.delete()
    return redirect('user_list')

#User
def user_list(request):
    users = User.objects.all()  
    return render(request, 'user_management/user_list.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_management/user_form.html', {'form': form} )


def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_management/user_form.html', {'form': form})


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')


