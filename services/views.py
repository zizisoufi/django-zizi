from django.shortcuts import render,get_object_or_404
from .models import Services, Specials
def services(request, **kwargs):
    #category = request.GET.get("category")
    if kwargs.get("cat"):
        services = Services.objects.filter(category__name=kwargs.get("cat"), status=True)
    elif kwargs.get("user"):
        services = Services.objects.filter(creator__username=kwargs.get("user"), status=True)
    elif request.GET.get("search"):
        services = Services.objects.filter(ltitle__contains=request.GET.get("search"), status=True)


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
        service.counted_view += 1
        service.save()
        context = {
             "service" : service
         }
        return render(request, "services/service-details.html", context=context)
    except:
        return render(request, "root/404.html", status=404 )
    
    
def service_null(request):
    return services(request)