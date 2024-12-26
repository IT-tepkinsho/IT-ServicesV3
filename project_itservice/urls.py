"""
URL configuration for project_itservice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('general.urls')),
    path('equipments/', include('equipment_management.urls')),
    path('requests/', include('service_requests.urls')),
    path('managements/', include('repair_management.urls')),
    path('users/', include('user_management.urls')),
    path('dashboard/', include('staff.urls')),
    path("select2/", include("django_select2.urls")),
    
]

if settings.DEBUG:  # ให้ทำเฉพาะเมื่ออยู่ในโหมดพัฒนา
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)