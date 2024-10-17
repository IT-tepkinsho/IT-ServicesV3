from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'serial_number', 'purchase_date', 'warranty_expiration']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'warranty_expiration': forms.DateInput(attrs={'type': 'date'}),
        }
