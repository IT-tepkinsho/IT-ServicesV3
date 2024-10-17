from django import forms
from .models import ServiceRequest, Repair, Claim

class ServiceRequestForm(forms.ModelForm):
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
            'request_description',
            'repair_by'
        ]
        widgets = {
            'repair_type': forms.Select(attrs={'class': 'form-select'}),
            'repair_title': forms.Select(attrs={'class': 'form-select'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'list': 'ownerList', 'autocomplete': 'off'}),
            'user_department': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'user_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'equipment': forms.TextInput(attrs={'class': 'form-control'}),
            'attached_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'request_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        # เพิ่มฟิลด์ request_date เป็น readonly
        request_date = forms.DateTimeField(required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['request', 'repair_details']

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['repair', 'claim_description', 'claim_status']
