from django.contrib import admin # type: ignore
from payments.models import Payment
from . import Payment

# Register your models here.
@admin.site.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'rental', 'user', 'amount_paid', 'payment_method', 'payment_status')
