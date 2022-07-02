from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from . models import Reservation, Room, Customer, Facility
from . forms import RoomUpdateForm

class AvailableRooms(ListView):
    template_name = 'available_rooms.html'
    model = Room
    context_object_name = 'available_rooms'

    def get_queryset(self):
        rooms = Room.objects.filter(availability = True)
        for room in rooms:
            print(room.facility.all())
        
        return rooms
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['facilities'] = Facility.objects.all()
        return super().get_context_data(**kwargs)

class RoomDetailView(DetailView):
    template_name = 'room_detail.html'
    model = Room
    pk_url_kwarg = 'room_no'
    context_object_name = 'room'


class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomUpdateForm
    template_name = 'room_update.html'
    pk_url_kwarg = 'room_no'
    context_object_name = 'room'



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



class ReservationDetailView(DetailView):
    template_name = 'reservation_detail.html'
    model = Reservation
    context_object_name = 'reservation'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = Room.objects.get(reservation = self.object.reservation_id)
        return super().get_context_data(**kwargs)


