from django.urls import path
from .views import (cancel_service_request, external_repair_form, get_repair_list, it_repair_form, new_device_form, service_request_detail, service_request_job_detail, service_request_list, 
    create_service_request, create_repair, create_claim, get_repair_topics, service_request_history, 
    get_repair_history, get_user_details, ticket_request, update_repair_details, update_status)
                    

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
    path('service-request/job/<int:service_request_id>/', service_request_job_detail, name='service_request_job'),
    path('update-status/', update_status, name='update_status'),
    path('update-repair-details/', update_repair_details, name='update_repair_details'),
    path('it-repair-form/', it_repair_form, name='it-repair-form'),
    path('external-repair-form/', external_repair_form, name='external-repair-form'),
    path('new-device-form/', new_device_form, name='new_device_form'),
    path('ticket-request/', ticket_request, name='ticket_request'),
]

