from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .serializers import CarSerializer
from .models import Car
from rest_framework import generics

# Create your views here.


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    @method_decorator(cache_page(60 * 60 * 2))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs) 
    
    
class CarDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer    
