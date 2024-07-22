from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'cars.html'

class CarsListView(ListView):
    model = Car
    template_name = "cars_list.html"
    context_object_name = "cars_objs"

class CarDetailsView(DetailView):
    model = Car
    template_name = "car_details.html"

class CarCreateView(CreateView):
    model = Car
    template_name = 'car_create.html'
    fields = ['brand', 'model', 'price', 'is_bought', 'buy_time', 'buyer_id']

class CarUpdateView(UpdateView):
    model = Car
    template_name = "car_update.html"
    fields = "__all__"

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('cars_list')
