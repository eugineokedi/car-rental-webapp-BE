from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .serializers import CarSerializer
from .models import Car
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.exceptions import NotFound

# Create your views here.


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['brand', 'model']
    ordering_fields = ['year', 'date_created']
    
    @method_decorator(cache_page(60 * 60 * 2))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs) 
    
    
class CarDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer 
    permission_classes = [IsAuthenticated]  
    
    
    def get_object(self):
        try:
            return super().get_object()
        except Car.DoesNotExist:
            raise NotFound("The requested car does not exist.") 
