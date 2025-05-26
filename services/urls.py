from django.urls import path
from .views import create_service,service_list,request_service,user_dashboard,service_detail

urlpatterns = [
    path('create/', create_service, name='create_service'),
    path('', service_list, name='service_list'),
    path('request/<int:service_id>/', request_service, name='request_service'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('services/<int:service_id>/', service_detail, name='service_detail'),


]
