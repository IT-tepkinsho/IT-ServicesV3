from django.urls import path
from .views import repair_type_list, create_repair_type, edit_repair_type, delete_repair_type, repair_topic_list, create_repair_topic, edit_repair_topic, delete_repair_topic

urlpatterns = [
    path('', repair_type_list, name='repair_type_list'),
    path('create/', create_repair_type, name='create_repair_type'),
    path('edit/<int:pk>/', edit_repair_type, name='edit_repair_type'),
    path('delete/<int:pk>/', delete_repair_type, name='delete_repair_type'),
    path('topics/', repair_topic_list, name='repair_topic_list'),
    path('topics/create/', create_repair_topic, name='create_repair_topic'),
    path('topics/edit/<int:pk>/', edit_repair_topic, name='edit_repair_topic'),
    path('topics/delete/<int:pk>/', delete_repair_topic, name='delete_repair_topic'),
]
