from django.http import JsonResponse
# AJAX endpoint for doctor name/location suggestions
def doctor_suggestions(request):
    query = request.GET.get('q', '')
    suggestions = []
    if query:
        doctors = Doctor.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(location__icontains=query)
        )[:5]
        for doc in doctors:
            suggestions.append({'name': doc.name, 'location': doc.location})
    return JsonResponse({'suggestions': suggestions})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import models
from .models import Doctor

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    query = request.GET.get('q', '')
    if query:
        doctors = Doctor.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(location__icontains=query)
        )
    else:
        doctors = Doctor.objects.all()
    return render(request, 'dashboard.html', {'doctors': doctors, 'query': query})

def login_view(request):
    message = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        else:
            message = 'Invalid username or password. Please try again.'
    return render(request, 'login.html', {'message': message})

def register_view(request):
    message = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            message = 'Username already exists. Please choose another.'
        elif len(password) < 4:
            message = 'Password must be at least 4 characters.'
        else:
            User.objects.create_user(username=username, password=password)
            message = 'Registration successful! Please login.'
            return render(request, 'register.html', {'message': message})
    return render(request, 'register.html', {'message': message})

def logout_view(request):
    logout(request)
    return redirect('/')

def profile(request):
    return render(request, 'profile.html')