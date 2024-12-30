from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

# Create your models here.

payment_choices = (
    ('mpesa', 'Mpesa'),
    ('card', 'Credit Card'),
    ('Cash', 'Cash'),
    ('transfer', 'Bank Transfer'),
)

status_choices = (
    ('completed', 'Completed'),
    ('pending', 'Pending'),
    ('failed', 'Failed'),
    ('refunded', 'Refunded'),
    ('cancelled', 'Cancelled'),
)
class Payment(models.Model):
    # Relationship
    rental = models.ForeignKey('Rental', on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    
    # Payment details
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=payment_choices)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    payment_status = models.CharField(max_length=50, choices=status_choices, default='Pending')
    notes = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['-payment_date']
    
    def __str__(self):
        return f"Payment {self.transaction_id} - {self.payment_status} - {self.amount}"
