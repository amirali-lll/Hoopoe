from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=30)
    feature_summery_title = models.CharField(max_length=300,blank=True)
    feature_summery1 = models.CharField(max_length=300,blank=True)
    feature_summery2 = models.CharField(max_length=300,blank=True)
    feature_summery3 = models.CharField(max_length=300,blank=True)
    feature_summery4 = models.CharField(max_length=300,blank=True)

    main_titel = models.CharField(max_length=300,blank=True)
    main_description = models.TextField(blank=True)
    


    feature1_title = models.CharField(max_length=30,blank=True)
    feature1_description = models.TextField(blank=True)
    feature1_image = models.ImageField(blank=True)
    
    feature2_title = models.CharField(max_length=30,blank=True)
    feature2_description = models.TextField(blank=True)
    feature2_image = models.ImageField(blank=True)

    feature3_title = models.CharField(max_length=30,blank=True)
    feature3_description = models.TextField(blank=True)
    feature3_image = models.ImageField(blank=True)

    def get_absolute_url(self):
        return f"/services/{self.id}"
