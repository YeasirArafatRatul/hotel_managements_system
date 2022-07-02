from django.urls import path
from . import views



app_name = 'reservation'

urlpatterns = [
    path('available-rooms', views.AvailableRooms.as_view(), name='rooms'),
    path('room-detail/<int:room_no>', views.RoomDetailView.as_view(), name='room-detail'),
    path('room-update/<int:room_no>', views.RoomUpdateView.as_view(), name='room-update'),
    path('reservation', views.ReservationView.as_view(), name='reservation'),
    path('reservation-detail/<int:pk>', views.ReservationDetailView.as_view(), name='reservation-detail'),
]