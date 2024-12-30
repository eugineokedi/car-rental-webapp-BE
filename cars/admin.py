from django.contrib import admin # type: ignore
from . import Car

# Register your models here.
@admin.site.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_brand', 'car_model', 'year', 'registration_number', 'image')
