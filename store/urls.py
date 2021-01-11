from django.urls import path, include
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product/<slug>/', views.ProductView.as_view(), name='product'),
    path('chart/', views. , name='chart')
    ]
