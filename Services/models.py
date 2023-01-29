from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=32,primary_key=True)
    title = models.CharField(max_length=256,blank=True)
    overview_title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    # features | FK
    # overviews | FK
    def get_absolute_url(self):
        return f"/services/{self.name}"


class Feature(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='features')
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)


class ServiceOverview(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='overviews')
    text = models.CharField(max_length=512)

