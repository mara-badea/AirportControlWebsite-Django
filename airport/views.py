from django.shortcuts import render
from .models import Schedule

# Create your views here.


def schedule_view(request):
    context = {
        'schedule' : Schedule.objects.all()
    }
    return render(request, 'airport/home.html', context)

