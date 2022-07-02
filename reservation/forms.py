from django import forms
from . models import Room

class RoomUpdateForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ('image','room_no')