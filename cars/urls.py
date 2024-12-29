from django.urls import path # type: ignore
from . import views


urlpatterns = [
    path('car_list/', views.CarList.as_view(), name="car_list"),
    path('car_detail/', views.CarDetails.as_view(), name="car_detail"),
]
