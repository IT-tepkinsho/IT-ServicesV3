from django.urls import path
from .views import (cancel_service_request, get_repair_list, service_request_detail, service_request_list, 
    create_service_request, create_repair, create_claim, get_repair_topics, service_request_history, 
    get_repair_history, get_user_details)
                    

urlpatterns = [
    path('', service_request_list, name='service_request_list'),
    path('history/', service_request_history, name='service_request_history'),
    path('create/', create_service_request, name='create_service_request'),
    path('repair/create/<int:request_id>/', create_repair, name='create_repair'),
    path('claim/create/<int:repair_id>/', create_claim, name='create_claim'),
    path('get-repair-topics/', get_repair_topics, name='get_repair_topics'),
    path('get-repair-history/', get_repair_history, name='get_repair_history'),
    path('get-repair-list/', get_repair_list, name='get_repair_list'),
    path('get-user-details/', get_user_details, name='get_user_details'),
    path('service-request/<int:service_request_id>/', service_request_detail, name='service_request_detail'),
    path('service-request/cancel/<int:pk>/', cancel_service_request, name='cancel_service_request'),
]

