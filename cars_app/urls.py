from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('cars/<int:pk>/', CarDetailsView.as_view(), name="car_details"),
    path('cars/create/', CarCreateView.as_view(), name='car_create'),
    path('cars/update/<int:pk>/', CarUpdateView.as_view(), name="car_update"),
    path('cars/delete/<int:pk>/', CarDeleteView.as_view(), name="car_delete")
]
