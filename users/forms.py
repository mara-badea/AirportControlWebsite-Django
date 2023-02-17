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

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['flight_number', 'origin', 'destination', 'departure_date', 'departure_time',
                  'arrival_date', 'arrival_time', 'price']

class EditTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['flight_number', 'origin', 'destination', 'departure_date', 'departure_time',
                  'arrival_date', 'arrival_time', 'departure_date', 'price']

class TicketPurchaseForm(forms.ModelForm):
    class Meta:
        model = TicketPurchase
        fields = ['profile', 'ticket']

class SearchFlightForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['flight_number', 'origin', 'destination', 'departure_time', 'estimated_departure',
                  'arrival_time', 'estimated_arrival', 'day', 'status']


class TicketSearchForm(forms.Form):
    origin = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)
    departure_date = forms.DateField()
    return_date = forms.DateField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['return_date'].widget.attrs['class'] = 'optional-field'

    def search(self):
        tickets = Ticket.objects.filter(origin=self.cleaned_data['origin'],
                                         destination=self.cleaned_data['destination'],
                                         departure_date=self.cleaned_data['departure_date'])

        if self.cleaned_data.get('return_date'):
            tickets = tickets.filter(arrival_date=self.cleaned_data['return_date'])

        return tickets

class TicketPurchaseForm(forms.ModelForm):
    class Meta:
        model = TicketPurchase
        fields = []

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.ticket = kwargs.pop('ticket')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        ticket_purchase = super().save(commit=False)
        ticket_purchase.profile = self.user.profile
        ticket_purchase.ticket = self.ticket

        if commit:
            ticket_purchase.save()

        return ticket_purchase
