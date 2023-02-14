from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Flight, Ticket, TicketPurchase
from airport.models import Schedule

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['tickets']

class FlightForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['flight_number', 'origin', 'destination', 'departure_time', 'estimated_departure',
                  'arrival_time', 'estimated_arrival', 'day', 'status']

class EditFlightForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['flight_number', 'origin', 'destination', 'departure_time', 'estimated_departure',
                  'arrival_time', 'estimated_arrival', 'day', 'status']

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['flight_number', 'origin', 'destination', 'departure_date', 'departure_time',
                  'arrival_date', 'arrival_time']

class TicketPurchaseForm(forms.ModelForm):
    class Meta:
        model = TicketPurchase
        fields = ['profile', 'ticket']

class SearchFlightForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['flight_number', 'origin', 'destination', 'departure_time', 'estimated_departure',
                  'arrival_time', 'estimated_arrival', 'day', 'status']
