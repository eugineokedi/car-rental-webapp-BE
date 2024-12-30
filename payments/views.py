from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.exceptions import NotFound
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .serializers import PaymentSerializer
from .models import Payment

# Create your views here.
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    
    @method_decorator(cache_page(60 * 60 * 2))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class PaymentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        try:
            return super().get_object()
        except Payment.DoesNotExist:
            raise NotFound("The requested payment does not exist.")    
