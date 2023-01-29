from django.shortcuts import render,get_object_or_404
from Services.models import Service

# Create your views here.
def dynamic_lookup(request,pk):
    # service = Service.objects.get(pk=pk)
    service = get_object_or_404(Service,pk=pk)
    # services = Service.objects.all()
    context = {
        'service':service,
        # 'services':services
    }
    return render(request,'service.html',context)