from django.urls import path
from . import views

urlpatterns = [
    path('payment_list', views.PaymentList.as_view(), name='payment_list'),
    path('payment_details', views.PaymentDetails.as_view(), name='payment_details'),
]
