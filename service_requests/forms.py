from django import forms
from .models import RepairClaim, RepairUpdateLog, ServiceRequest, Repair, RepairClaim, RequestStatus, RepairType
from user_management.models import User, Department
from django.utils import timezone

class ServiceRequestForm(forms.ModelForm):
    request_date = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
        initial=timezone.now
    )

    user_name = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select select2', 'id': 'user_name_select'}),
        required=True
    )


    class Meta:
        model = ServiceRequest
        fields = [
            'repair_type',
            'repair_title',
            'user_name',
            'user_department',
            'user_contact',
            'equipment',
            'attached_file',
            'request_description'
        ]
        widgets = {
            'repair_type': forms.Select(attrs={'class': 'form-select'}),
            'repair_title': forms.Select(attrs={'class': 'form-select'}),
            'user_department': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'id': 'id_user_department'}),
            'user_contact': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_user_contact'}), 
            'equipment': forms.TextInput(attrs={'class': 'form-control'}),
            'attached_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'request_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class RepairForm(forms.ModelForm):
    class Meta:
        model = RepairUpdateLog
        fields = ['service_request', 'details']


class ClaimForm(forms.ModelForm):
    class Meta:
        model = RepairClaim
        fields = [
            'service_request', 'company', 'claim_date', 
            'vehicle_type', 'license_plate', 'purpose_of_out', 
            'equipment', 'cost', 'claim_status'
        ]
        widgets = {
            'service_request': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'claim_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'vehicle_type': forms.TextInput(attrs={'class': 'form-control'}),
            'license_plate': forms.TextInput(attrs={'class': 'form-control'}),
            'purpose_of_out': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'equipment': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'claim_status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        service_request_instance = kwargs.pop('service_request_instance', None)
        super().__init__(*args, **kwargs)

        # เพิ่มการตั้งค่า initial สำหรับ 'equipment'
        service_request = kwargs.get('initial', {}).get('service_request')
        if service_request:
            kwargs['initial']['equipment'] = service_request.equipment

        if service_request_instance:
            self.fields['service_request'].initial = service_request_instance.id
            self.fields['equipment'].initial = service_request_instance.equipment


class RepairDetailForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = [
            'method_of_repair',
            'repair_by',
            'cost',
            'equipment',
            'change_device',
            'equipment_new',
            'operator'
        ]
        widgets = {
            'method_of_repair': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'equipment': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'change_device': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'equipment_new': forms.TextInput(attrs={'class': 'form-control'}),
            'operator': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ตั้งค่า operator จาก session
        if 'initial' in kwargs and 'operator' in kwargs['initial']:
            self.fields['operator'].initial = kwargs['initial']['operator']