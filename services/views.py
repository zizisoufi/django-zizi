from django.shortcuts import render
from .models import Services, Specials
def services(request):
    services = Services.objects.filter(status=True)
    specials = Specials.objects.filter(status=True)
    context = {
        
        "services" : services,
         "specials" : specials,
    }
    return render(request, "services/services.html", context=context)
