# equipment_management/forms.py
from django import forms
from .models import (CameraCCTV, Equipment, Computer, Monitor, Mouse, Keyboard, Network, Printer, Scanner, 
                        Server, Software, GroupProgram, Ups, Tablet, Other)

from django.forms import formset_factory
from django_select2.forms import Select2MultipleWidget
from django_select2.forms import ModelSelect2Widget
from django_select2.forms import Select2Widget

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'equipment_type', 'serial_number', 'purchase_date', 'warranty_expiration', 'status']

class ComputerForm(forms.ModelForm):

    software = forms.ModelMultipleChoiceField(
        queryset=Software.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )
 
    class Meta:
        model = Computer
        fields = '__all__'
        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'spec': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'internet_connection': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'equipment_status': forms.Select(attrs={'class': 'form-control'}),
            'equipment_condition': forms.Select(attrs={'class': 'form-control'}),
            'vendor': forms.Select(attrs={'class': 'form-control select2'}),
            'other': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'monitor': forms.Select(attrs={'class': 'form-control select2'}),
            'monitor_model': forms.TextInput(attrs={'class': 'form-control'}),
            'keyboard': forms.Select(attrs={'class': 'form-control select2'}),
            'keyboard_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'mouse': forms.Select(attrs={'class': 'form-control select2'}),
            'mouse_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'printer': forms.Select(attrs={'class': 'form-control select2'}),
            'printer_model': forms.TextInput(attrs={'class': 'form-control'}),
            'ups': forms.Select(attrs={'class': 'form-control select2'}),
            'ups_model': forms.TextInput(attrs={'class': 'form-control'}),
            'scanner': forms.Select(attrs={'class': 'form-control select2'}),
            'scanner_model': forms.TextInput(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control select2'}),
            'owner': forms.Select(attrs={'class': 'form-control select2'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'program': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น AutoCAD, line, etc.'})
        }

    def __init__(self, *args, **kwargs):
        super(ComputerForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'

        widgets = {
           'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'version':  forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'license_key': forms.TextInput(attrs={'class': 'form-control'}),
            'group_program': forms.Select(attrs={'class': 'form-control'}),
            'software_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
            'computer': forms.Select(attrs={'class': 'form-control'}),
            'other': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(SoftwareForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'

        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'warranty': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
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
        fields = '__all__'

        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'connection_type': forms.Select(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(MouseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = '__all__'

        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'connection_type': forms.Select(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(KeyboardForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = '__all__'

        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'print_type': forms.Select(attrs={'class': 'form-control'}),
            'warranty': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PrinterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class ScannerForm(forms.ModelForm):
    class Meta:
        model = Scanner
        fields = '__all__'

        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'warranty': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ScannerForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = '__all__'

        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'spec': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'warranty': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'ibm_warranty': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ServerForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class ProgramForm(forms.ModelForm):
    class Meta:
        model = GroupProgram
        fields = ['name'] 

class UpsForm(forms.ModelForm):
    class Meta:
        model = Ups
        fields = '__all__'

        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'warranty': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
        }

class NetworkForm(forms.ModelForm):
    class  Meta:
        model = Network
        fields = '__all__'

        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'warranty': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(NetworkForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class CameraCCTVForm(forms.ModelForm):
    class Meta:
        model = CameraCCTV
        fields = '__all__'
        
        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'warranty': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),

        }
    def __init__(self, *args, **kwargs):
        super(CameraCCTVForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class TabletForm(forms.ModelForm):
    class Meta:
        model = Tablet
        fields = '__all__'
        
        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'warranty': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),

        }
    def __init__(self, *args, **kwargs):
        super(TabletForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = '__all__'
        
        widgets = {
            'equipment_code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'warranty': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'vendor': forms.Select(attrs={'class': 'form-control'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'equipment_type': forms.Select(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),

        }
    def __init__(self, *args, **kwargs):
        super(OtherForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False