from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Car(models.Model):
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=255)
    year = name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)
    
