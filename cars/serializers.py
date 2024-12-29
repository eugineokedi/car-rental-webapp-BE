from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class meta:
        model = Car
        field = '__all__'