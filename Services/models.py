from unicodedata import name
from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
