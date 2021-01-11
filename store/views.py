from django.shortcuts import render
from .models import Item

def HomePage(request):
    context = {
            'items' : Item.objects.all()
            }
    return render(request, "mainPage.html", context)

def Product(request):
    context = {
            'items' : Item.objects.all()
            }
    return render(request, "mainPage.html", context)
