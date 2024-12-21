from django.shortcuts import render
from .models import Car

# Create your views here.

def index(request):
    car_images = Car.objects.all()
    cloudinary_img = {"car_images": car_images}
    return render(request, 'index.html', cloudinary_img=cloudinary_img)
