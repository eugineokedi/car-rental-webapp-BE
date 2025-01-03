from django.contrib import admin
from .models import Car

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'year', 'registration_number', 'image')

