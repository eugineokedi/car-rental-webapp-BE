from rental.models import Rental
from rest_framework import serializers # type: ignore

class RentalSerializer(serializers.ModelSerializer):
    class meta:
        models = Rental
        fields = '__all__'