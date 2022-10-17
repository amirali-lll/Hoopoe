from django.shortcuts import render,get_object_or_404
from Services.models import Service

# Create your views here.
def dynamic_lookup(request,id):
    service = Service.objects.get(id=id)
    service = get_object_or_404(Service,id=id)
    services = Service.objects.all()

    context = {
        'service':service,
        'services':services
    }
    return render(request,'service.html',context)