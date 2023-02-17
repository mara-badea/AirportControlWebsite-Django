from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, FlightForm, EditFlightForm, TicketUpdateForm, TicketForm, EditTicketForm, TicketSearchForm, TicketPurchaseForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Ticket, Flight, TicketPurchase
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

@staff_member_required
def add_tickets(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.save()
            return redirect('manage-tickets')
    else:
        form = TicketForm()
        return render(request, 'airport/addtickets.html', {'form': form})

@staff_member_required
def edit_tickets(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = EditTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('manage-tickets')

    else:
        form = EditTicketForm(instance=ticket)
        return render(request, 'airport/edittickets.html', {'form': form})
    return render(request, 'airport/managetickets.html', {'form': form})

@staff_member_required
def delete_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('manage-tickets')
    return render(request, 'airport/deleteticket.html', {'ticket': ticket})
@login_required
def ticket_search(request):
    if request.method == 'POST':
        form = TicketSearchForm(request.POST)
        if form.is_valid():
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            departure_date = form.cleaned_data['departure_date']
            return_date = form.cleaned_data.get('return_date')

            tickets = Ticket.objects.filter(
                origin=origin,
                destination=destination,
                departure_date=departure_date,
            )
            if return_date:
                tickets = tickets.filter(arrival_date=return_date)

            return render(request, 'airport/ticket_search_results.html', {'tickets': tickets})
    else:
        form = TicketSearchForm()

    return render(request, 'airport/buyticket.html', {'form': form})


@login_required
def purchase_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            profile = request.user.profile
            purchase = TicketPurchase.objects.create(
                profile=profile,
                ticket=ticket,
            )
            return render(request, 'ticket_purchase_success.html', {'purchase': purchase})
    else:
        form = TicketPurchaseForm()

    return render(request, 'ticket_purchase.html', {'form': form, 'ticket': ticket})





