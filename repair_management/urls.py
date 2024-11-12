from django.urls import path
from .views import (create_vendor, repair_type_list, create_repair_type, edit_repair_type, delete_repair_type, repair_topic_list, 
                    create_repair_topic, edit_repair_topic, delete_repair_topic, vendor_list, vendor_update, vendor_delete)

urlpatterns = [
    path('', repair_type_list, name='repair_type_list'),
    path('create/', create_repair_type, name='create_repair_type'),
    path('edit/<int:pk>/', edit_repair_type, name='edit_repair_type'),
    path('delete/<int:pk>/', delete_repair_type, name='delete_repair_type'),
    path('topics/', repair_topic_list, name='repair_topic_list'),
    path('topics/create/', create_repair_topic, name='create_repair_topic'),
    path('topics/edit/<int:pk>/', edit_repair_topic, name='edit_repair_topic'),
    path('topics/delete/<int:pk>/', delete_repair_topic, name='delete_repair_topic'),
    path('vendors/', vendor_list, name='vendor_list'),
    path('vendors/create/', create_vendor, name='create_vendor'),
    path('vendors/update/<int:pk>', vendor_update, name='vendor_update'),
    path('vendors/delete/<int:pk>/', vendor_delete, name='vendor_delete')
]
