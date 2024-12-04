from django import forms
from .models import RepairUpdateLog, ServiceRequest, Repair, Claim, RequestStatus, RepairType
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
        model = Claim
        fields = ['repair', 'claim_description', 'claim_status']


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