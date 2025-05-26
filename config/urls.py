from django.contrib import admin
from django.urls import path, include
from services.views import service_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')), 
    path('services/', include('services.urls')),
    path('', service_list, name='home'),


]
