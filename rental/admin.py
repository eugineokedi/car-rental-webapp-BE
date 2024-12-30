from django.contrib import admin # type: ignore
from .models import Rental

# Register your models here.
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'daily_rate', 'total_cost', 'notes')
