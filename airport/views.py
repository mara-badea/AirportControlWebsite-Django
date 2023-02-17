from django.shortcuts import render
from .models import Schedule
from users.models import Ticket

# Create your views here.


def schedule_view(request):

    context = {
        'schedule' : Schedule.objects.all().order_by('departure_time')
    }
    return render(request, 'airport/home.html', context)

def ticket_view(request):

    context = {
        'ticket' : Ticket.objects.all().order_by('departure_date', 'departure_time')
    }
    return render(request, 'airport/managetickets.html.', context)


