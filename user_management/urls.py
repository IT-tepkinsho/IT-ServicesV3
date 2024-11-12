from django.urls import path
from .views import (user_list, create_user, edit_user, delete_user, department_list, create_department, edit_department, 
                    delete_department )

urlpatterns = [
    path('', user_list, name='user_list'),
    path('create/', create_user, name='create_user'),
    path('edit/<int:pk>/', edit_user, name='edit_user'),
    path('delete/<int:pk>/', delete_user, name='delete_user'),
    path('departments/', department_list, name='department_list'),
    path('departments/create/', create_department, name='create_department'),
    path('departments/edit/<int:pk>/', edit_department, name='edit_department'),
    path('departments/delete/<int:pk>/', delete_department, name='delete_department'),
  
    
]
