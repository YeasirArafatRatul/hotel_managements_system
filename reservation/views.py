from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404 
from . models import Reservation

# Create your views here.

class ReservationView(CreateView):
    template_name = 'reservation.html'
    model = Reservation

    fields = ['customer', 'no_of_children', 'no_of_adults', 'reservation_date_time', 'expected_arrival_date_time', 'expected_departure_date_time']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        request = self.request
        form.instance.staff = request.user
        return super().form_valid(form)