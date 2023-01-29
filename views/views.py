from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Services.models import Service

def index(request):
     template = loader.get_template('index.html')
     services = Service.objects.all()
     context = {
          'services':services
     }
     return HttpResponse(template.render(context, request))

def contact(request):
     template = loader.get_template('contact.html')
     context = {}
     return HttpResponse(template.render(context, request))
