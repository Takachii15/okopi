from django.urls import path, include
from django.conf import settings
from . import views


urlpatterns = [
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.LoginPage, name='login'),
    ]
