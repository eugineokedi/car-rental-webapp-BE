from rest_framework import serializers # type: ignore
from payments.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Payment
        fields = "__all__"