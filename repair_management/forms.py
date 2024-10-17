from tkinter import Widget
from django import forms
from .models import RepairType, RepairTopic

class RepairTypeForm(forms.ModelForm):
    class Meta:
        model = RepairType
        fields = ['name']


class RepairTopicForm(forms.ModelForm):
    class Meta:
        model = RepairTopic
        fields = ['name', 'repair_type']
        widgets = {
            'repair_type': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
