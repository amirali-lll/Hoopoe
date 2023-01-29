from django.contrib import admin
from .models import Service,Feature
# Register your models here.

# admin.site.register(Service,ServiceAdmin)

class FeatureInline(admin.StackedInline):
    model = Feature
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    
    list_display=('name',)
    inlines = [FeatureInline]


