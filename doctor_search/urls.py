from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('profile/', views.profile),
    path('register/', views.register_view),
    path('doctor-suggestions/', views.doctor_suggestions, name='doctor_suggestions'),
]