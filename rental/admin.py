from django.contrib import admin
from .rental import Rental

# Register your models here.
@admin.site.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'user', 'start_date', 'end_date', 'status')
