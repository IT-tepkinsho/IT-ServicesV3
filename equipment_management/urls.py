from django.urls import path
from .views import equipment_list, equipment_add, equipment_edit

urlpatterns = [
    path('', equipment_list, name='equipment_list'),
    path('add/', equipment_add, name='equipment_add'),
    path('edit/<int:pk>/', equipment_edit, name='equipment_edit'),
]
