
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q, Count
from .models import Doctor

# AJAX endpoint for doctor name/location suggestions
def doctor_suggestions(request):
    query = request.GET.get('q', '')
    suggestions = []
    if query:
        doctors = Doctor.objects.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query)
        )[:5]
        for doc in doctors:
            suggestions.append({'name': doc.name, 'location': doc.location})
    return JsonResponse({'suggestions': suggestions})

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    # Build base queryset with filters
    doctors = Doctor.objects.all()
    query = request.GET.get('q', '')
    spec_filter = request.GET.get('spec', '')
    loc_filter = request.GET.get('loc', '')

    if query:
        doctors = doctors.filter(Q(name__icontains=query) | Q(location__icontains=query))
    if spec_filter:
        doctors = doctors.filter(specialization__icontains=spec_filter)
    if loc_filter:
        doctors = doctors.filter(location__icontains=loc_filter)

    total_doctors = doctors.count()
    specialty_stats = dict(
        doctors.values('specialization').annotate(count=Count('id'))
        .values_list('specialization', 'count')
    )
    featured_doctors = doctors[:3]

    return render(request, 'dashboard.html', {
        'doctors': doctors,
        'query': query,
        'spec_filter': spec_filter,
        'loc_filter': loc_filter,
        'total_doctors': total_doctors,
        'specialty_stats': specialty_stats,
        'featured_doctors': featured_doctors
    })

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