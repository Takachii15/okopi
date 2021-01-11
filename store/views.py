from django.shortcuts import render
from django.views.generic import ListView, DetailView
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


class HomeView(ListView):
    model = Item
    template_name = "mainPage.html"


class ProductView(DetailView):
    model = Item
    template_name = ""

