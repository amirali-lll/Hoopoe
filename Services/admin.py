from django.contrib import admin
from .models import Service,Feature,ServiceOverview
# Register your models here.

# admin.site.register(Service,ServiceAdmin)


class ServiceOverviewInline(admin.TabularInline):
    model = ServiceOverview
    extra = 1


class FeatureInline(admin.StackedInline):
    model = Feature
    extra = 1
    
    


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    
    list_display=('name',)
    inlines = [ServiceOverviewInline,FeatureInline]





