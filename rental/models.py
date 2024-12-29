from django.db import models
from datetime import timedelta
from django.contrib.auth import get_user_model

# Associating rentals with users
User = get_user_model()

# Create your models here.
class Rental(models.Model):
    # Relationship
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='rentals')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals')
    
    # Rental period
    start_date = models.DateField()
    end_date = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    
    # Rental cost
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Status
    is_active = models.BooleanField(default=True)
    returned = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    
    # Timestamps
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    # Most recent bookings appear first
    class meta:
        ordering = ['-booking_date']
        
    def __str__(self):
        return f"Rental: {self.car} by {self.user} from {self.start_date} to {self.end_date}" 
    
    # Calculate total cost based on rental period and daily rate
    def save(self, *args, **kwargs):
        if self.start_date and self.end_date and self.daily_rate:
            rental_days = (self.end_date - self.start_date).days
            self.total_cost = rental_days * self.daily_rate
        super().save(*args, **kwargs)
        
    # Calculate rental duration
    def rental_duration(self):
        return (self.end_date - self.start_date).days if self.end_date and self.start_date else 0            
