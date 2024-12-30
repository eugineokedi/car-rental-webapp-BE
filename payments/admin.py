from django.contrib import admin # type: ignore
from .models import Payment

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount_paid', 'payment_method', 'payment_date', 'payment_status', 'notes')

