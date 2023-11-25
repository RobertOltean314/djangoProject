from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from cars.forms import CarForm, CarUpdateForm
from cars.models import Car


# Create your views here.

class CarCreateView(LoginRequiredMixin, CreateView):
    template_name = 'car/create_car.html'
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('home')


class CarListView(LoginRequiredMixin, ListView):
    template_name = 'car/list_of_cars.html'
    model = Car
    context_object_name = 'all_cars'


class CarUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'car/update_car.html'
    model = Car
    form_class = CarUpdateForm
    success_url = reverse_lazy('list-of-cars')


class CarDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'car/delete_car.html'
    model = Car
    success_url = reverse_lazy('list-of-cars')

class CarDetailView(LoginRequiredMixin, DetailView):
    template_name = 'car/details_car.html'
    model = Car
