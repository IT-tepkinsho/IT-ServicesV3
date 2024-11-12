from django.urls import path
from .views import computer_create, computer_delete, computer_list, computer_update, equipment_list, equipment_create, equipment_update, equipment_delete, monitor_create, monitor_list

urlpatterns = [
    path('', equipment_list, name='equipment_list'),
    path('create/', equipment_create, name='equipment_create'),
    path('update/<int:pk>/', equipment_update, name='equipment_update'),
    path('delete/<int:pk>/', equipment_delete, name='equipment_delete'),
    path('computer/', computer_list, name='computer_list'),
    path('computer/create/', computer_create, name='computer_create'),
    path('computer/update/<int:pk>/', computer_update, name='computer_update'),
    path('computer/delete/<int:pk>/', computer_delete, name='computer_delete'),
    path('monitors/', monitor_list, name='monitor_list'),
    path('monitors/create/', monitor_create, name='monitor_create'),
]
