from django.shortcuts import render,get_object_or_404
from .models import Services, Specials
def services(request):
    category = request.GET.get("category")
    if category:
        services = Specials.objects.filter(category__name=category, status=True)
    else:
         services = Services.objects.filter(status=True)
    specials = Specials.objects.filter(status=True)
    context = {
        
        "services" : services,
        "specials" : specials,
     }
    return render(request, "services/services.html", context=context)

def service_detail(request, id): 
    try:                 
        service =get_object_or_404(Services, pk=id)
        context = {
             "service" : service
         }
        return render(request, "services/service-details.html", context=context)
    except:
        return render(request, "root/404.html", status=404 )
    
    
def service_null(request):
    return services(request)