from django.db import models


# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100, db_index=True)
    model = models.CharField(max_length=255)
    year = models.IntegerField(db_index=True)
    registration_number = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['brand', 'year']),
            models.Index(fields=['date_created']),
        ]
    
    def __str__(self):
        return f'<{self.car_brand}, {self.car_model}, {self.year}, {self.registration_number}, {self.description}, {self.image}>'
    
