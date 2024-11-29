from tkinter import Widget
from django import forms
from .models import RepairType, RepairTopic, Vendor

class RepairTypeForm(forms.ModelForm):
    class Meta:
        model = RepairType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RepairTopicForm(forms.ModelForm):
    class Meta:
        model = RepairTopic
        fields = ['name', 'repair_type']
        widgets = {
            'repair_type': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),

        }

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_code', 'vendor_name', 'vendor_phone', 'email']
        widgets = {
            'vendor_code': forms.TextInput(attrs={'class': 'form-control'}),
            'vendor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'vendor_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }