from django.shortcuts import render
from .models import Exercise

def index(request):
    items = Exercise.objects.all() 
    return render(request, "core/index.html", {"items": items})
# Create your views here.

def contact(request):
    return render(request, "core/contact.html")


def about(request):
    return render(request, "core/about.html")