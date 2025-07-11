from django.shortcuts import render
from .models import pricing,Leader

def home(request):
    return render(request, "home/index.html")

def contact(request):
    return render(request, "home/contact.html")

def about(request):
    leaders = Leader.objects.filter(status=True)
    context = {
        "leaders": leaders,
    }
    return render(request, "home/about.html", context=context)

def pricing(request):  # چون اسم pricing با مدل تداخله، بهتره اسم تابع رو عوض کنی
    return render(request, "home/pricing.html")
