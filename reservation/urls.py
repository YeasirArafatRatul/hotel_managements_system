from django.urls import path
from . import views



app_name = 'reservation'

urlpatterns = [
    path('reservation', views.ReservationView.as_view(), name='reservation'),
    path('available-rooms', views.AvailableRooms.as_view(), name='rooms'),
    path('reservation-detail/<int:pk>', views.ReservationDetailView.as_view(), name='reservation-detail'),
]