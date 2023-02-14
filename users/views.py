from django.db.models import Q
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
def edit_flights(request, id):
    schedule = Schedule.objects.get(id=id)
    if request.method == 'POST':
        # Get the flight instance based on the submitted data
        form = EditFlightForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = EditFlightForm(instance=schedule)
        return render(request, 'airport/editflights.html', {'form' : form})
    return render(request, 'airport/home.html', {'form': form})

@staff_member_required
def delete_flight(request, id):
    flight = Schedule.objects.get(id=id)
    if request.method == 'POST':
        flight.delete()
        return redirect('home')
    return render(request, 'airport/deleteflight.html', {'flight': flight})

@login_required
def search_flight(request):
    schedules =  Schedule.objects.all()
    sort_by = request.GET.get('sort_by')
    search_criteria = request.GET.get('search_criteria')
    if search_criteria:
        schedules = schedules.filter(Q(origin__icontains=search_criteria) |
                                 Q(destination__icontains=search_criteria) |
                                Q(flight_number__icontains=search_criteria) |
                                 Q(departure_time__icontains=search_criteria) |
                                 Q(departure_time__icontains=search_criteria) |
                                 Q(estimated_departure__icontains=search_criteria) |
                                 Q(arrival_time__icontains=search_criteria) |
                                 Q(estimated_arrival__icontains=search_criteria) |
                                 Q(day__icontains=search_criteria) |
                                 Q(status__icontains=search_criteria) )
    if sort_by:
        schedules = schedules.order_by(sort_by)
    return render(request, 'airport/searchflights.html', {'schedules': schedules})




