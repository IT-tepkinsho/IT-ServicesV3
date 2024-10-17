from django.urls import path
from .views import service_request_list, create_service_request, create_repair, create_claim, get_repair_topics

urlpatterns = [
    path('', service_request_list, name='service_request_list'),
    path('create/', create_service_request, name='create_service_request'),
    path('repair/create/<int:request_id>/', create_repair, name='create_repair'),
    path('claim/create/<int:repair_id>/', create_claim, name='create_claim'),
    path('get-repair-topics/', get_repair_topics, name='get_repair_topics'),
]
