from rest_framework import serializers # type: ignore
from payments.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    rental = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    
    class Meta:
        models = Payment
        fields = "__all__"