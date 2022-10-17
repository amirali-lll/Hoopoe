from django.shortcuts import render
from Services.models import Service

# Create your views here.
def dynamic_lookup(request,id):
    service = Service.objects.get(id=id)
    all_services = Service.objects.all()

    context = {
        'service':service,
        'all_services':all_services
    }
    return render(request,'service.html',context)