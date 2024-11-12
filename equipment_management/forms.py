# equipment_management/forms.py

from django import forms
from .models import Equipment, Computer, Monitor, Mouse, Keyboard, Printer, Scanner, Server, Software, Program

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'equipment_type', 'serial_number', 'purchase_date', 'warranty_expiration', 'status']

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['equipment_code', 'spec', 'brand', 'ip_address', 'internet_connection', 'equipment_status', 'equipment_condition', 'vendor', 'other', 'monitor',
                  'monitor_model', 'keyboard', 'keyboard_brand', 'mouse', 'mouse_brand', 'printer', 'printer_model', 'ups', 'ups_model', 'scanner', 'scanner_model', 
                  'software', 'software_name', 'license_key', 'purchase_date', 'equipment_type', 'owner']
        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'spec': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'internet_connection': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'equipment_status': forms.Select(attrs={'class': 'form-control'}),
            'equipment_condition': forms.Select(attrs={'class': 'form-control'}),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'other': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'monitor': forms.Select(attrs={'class': 'form-control'}),
            'monitor_model': forms.TextInput(attrs={'class': 'form-control'}),
            'keyboard': forms.Select(attrs={'class': 'form-control'}),
            'keyboard_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'mouse': forms.Select(attrs={'class': 'form-control'}),
            'mouse_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'printer': forms.Select(attrs={'class': 'form-control'}),
            'printer_model': forms.TextInput(attrs={'class': 'form-control'}),
            'ups': forms.Select(attrs={'class': 'form-control'}),
            'ups_model': forms.TextInput(attrs={'class': 'form-control'}),
            'scanner': forms.Select(attrs={'class': 'form-control'}),
            'scanner_model': forms.TextInput(attrs={'class': 'form-control'}),
            'software': forms.Select(attrs={'class': 'form-control'}),
            'software_name': forms.TextInput(attrs={'class': 'form-control'}),
            'license_key': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(ComputerForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ['equipment_code', 'brand', 'model', 'serial_number', 'cost', 'warranty', 'vendor', 'status', 'condition', 'equipment_type', 'owner']

        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'warranty': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'vendor': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(MonitorForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class MouseForm(forms.ModelForm):
    class Meta:
        model = Mouse
        fields = ['equipment_code', 'name', 'brand', 'model', 'connection_type', 'purchase_date', 'equipment_type', 'owner']

class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = ['equipment_code', 'name', 'brand', 'model', 'layout', 'connection_type', 'purchase_date', 'equipment_type', 'owner']

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['equipment_code', 'name', 'brand', 'model', 'serial_number', 'print_type', 'purchase_date', 'equipment_type', 'owner']

class ScannerForm(forms.ModelForm):
    class Meta:
        model = Scanner
        fields = ['equipment_code', 'name', 'brand', 'model', 'serial_number', 'purchase_date', 'equipment_type', 'owner']

class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['equipment_code', 'name', 'brand', 'model', 'cpu', 'ram_size', 'storage_size', 'purchase_date', 'equipment_type']

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['equipment_code', 'name', 'version', 'license_key', 'purchase_date', 'equipment_type', 'owner']

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['equipment_code', 'name', 'license_key', 'purchase_date', 'equipment_type', 'owner'] 
