from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Services.models import Service

def index(request):
     template = loader.get_template('index.html')
     context = {}
     return HttpResponse(template.render(context, request))

def products(request):
     template = loader.get_template('products.html')
     context = {}
     return HttpResponse(template.render(context, request))

def contact(request):
     template = loader.get_template('contact.html')
     context = {}
     return HttpResponse(template.render(context, request))


def SIEM(request):
     return render(request,'SIEM.html',{})

def SIEM(request):
     return render(request,'SIEM.html',{})

def Hoopin(request):
     return render(request,'Hoopin.html',{})

def HoopTest(request):
     return render(request,'HoopTest.html',{})

def HoopEye(request):
     return render(request,'HoopEye.html',{})



def Test(request):
     services = Service.objects.all()
     context = {
          'services' : services,
     }
     return render(request,'test.html',context)