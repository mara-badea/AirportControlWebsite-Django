from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, FlightForm, EditFlightForm, TicketUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Ticket, Flight
from airport.models import Schedule

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,
                                instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form,

        }
        return render(request, 'users/profile.html', context)

@staff_member_required
def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.save()
            return redirect('home')
    else:
        form = FlightForm()
        return render(request, 'airport/addflights.html', {'form': form})

@staff_member_required
def edit_flights(request, flight_number):
    schedule = Schedule.objects.get(flight_number=flight_number)
    if request.method == 'POST':
        # Get the flight instance based on the submitted data
        form = EditFlightForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('home', schedule.flight_number)
    else:
        form = EditFlightForm(instance=schedule)
    return render(request, 'airport/editflights.html', {'form': form})

@staff_member_required
def delete_flight(request, flight_number):
    flight = Schedule.objects.get(flight_number=flight_number)
    if request.method == 'POST':
        flight.delete()
        return redirect('home')
    return render(request, 'airport/deleteflight.html', {'flight': flight})
