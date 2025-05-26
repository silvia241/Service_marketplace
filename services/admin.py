from django.contrib import admin
from .models import Service, ServiceRequest

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'created_at')
    search_fields = ('title', 'description',)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('service', 'requester', 'created_at')
    search_fields = ('message',)
