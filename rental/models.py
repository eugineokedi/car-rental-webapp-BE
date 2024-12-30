from django.db import models # type: ignore
from datetime import timedelta
from django.contrib.auth import get_user_model # type: ignore

# Associating rentals with users
User = get_user_model()

# Create your models here.
class Rental(models.Model):
    # Relationship
    # car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='rentals')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals')
    
    # Rental period
    start_date = models.DateField()
    end_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    
    # Rental cost
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Late fee rate
    late_fee_per_day = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
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
    
    # Calculate total cost and late fee based on dates
    def save(self, *args, **kwargs):
        # Calculate rental days and total cost
        if self.start_date and self.end_date and self.daily_rate:
            rental_days = (self.end_date - self.start_date).days
            self.total_cost = rental_days * self.daily_rate
            
        # Calculate late fee if returned after the end_date
        if self.actual_return_date and self.actual_return_date > self.end_date:
            late_days = (self.actual_return_date - self.end_date).days
            self.late_fee = late_days * self.late_fee_per_day
        else:
            self.late_fee = 0
            
        super().save(*args, **kwargs)        
        
    # Calculate rental duration
    def rental_duration(self):
        """Calculate rental duration in days."""
        return (self.end_date - self.start_date).days if self.end_date and self.start_date else 0
    
    # Calculate Late return days 
    def late_days(self):
        """Calculate the number of late days, if any."""
        if self.actual_return_date and self.actual_return_date > self.end_date:
            return (self.actual_return_date - self.end_date).days
        return 0
    
                            
