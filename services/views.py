from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import ServiceForm,ServiceRequestForm
from .models import Service,ServiceRequest

@login_required
def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user
            service.save()
            messages.success(request, "Service posted successfully!")
            return redirect('service_list')
    else:
        form = ServiceForm()
    
    return render(request, 'create_service.html', {'form': form})

def service_list(request):
    services = Service.objects.all().order_by('-created_at')
    return render(request, 'service_list.html', {'services': services})

@login_required
def request_service(request, service_id):
    service = Service.objects.get(id=service_id)

    if service.provider == request.user:
        messages.error(request, "❌ You cannot request your own service.")
        return redirect('service_list')


    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.service = service
            service_request.requester = request.user
            service_request.save()
            messages.success(request, 'Service request submitted successfully.')
            return redirect('service_list')
    else:
        form = ServiceRequestForm()

    return render(request, 'request_service.html', {'form': form, 'service': service})

@login_required
def user_dashboard(request):
    my_services = Service.objects.filter(provider=request.user)
    my_requests = ServiceRequest.objects.filter(requester=request.user).order_by('-created_at')
    return render(request, 'dashboard.html', {
        'my_services': my_services,
        'my_requests': my_requests,
    })

@login_required
def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service_detail.html', {'service': service})


