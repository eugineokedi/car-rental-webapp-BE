from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
