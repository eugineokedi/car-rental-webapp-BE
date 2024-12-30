from rental.models import Rental
from rest_framework import serializers # type: ignore

class RentalSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class meta:
        models = Rental
        fields = '__all__'
        
    # Custom validation
    def validate(self, data):
        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError("End date cannot be earlier than start date.")
        return data    