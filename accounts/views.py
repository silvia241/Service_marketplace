# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken.")
            return redirect('signup')

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, "Signup successful. Welcome!")
        return redirect('home')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful. Welcome back!")
            return redirect('service_list')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')



