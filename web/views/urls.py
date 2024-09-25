from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]
'''
    # products
    path('products/', views.products, name='products'),
    path('products/SIEM', views.SIEM, name='products-SIEM'),
    path('products/Hoopin', views.Hoopin, name='products-Hoopin'),
    path('products/HoopTest', views.HoopTest, name='products-HoopTest'),
    path('products/HoopEye', views.HoopEye, name='products-HoopEye')
'''