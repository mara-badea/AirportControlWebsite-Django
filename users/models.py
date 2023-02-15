from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Flight(models.Model):
    flight_number = models.CharField(max_length=100, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    estimated_departure = models.TimeField()
    arrival_time = models.TimeField()
    estimated_arrival = models.TimeField()
    day = models.DateField()
    status = models.CharField(max_length=100)

class Ticket(models.Model):
    flight_number = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    price = models.CharField(max_length=100, blank=True, null=True)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket, through='TicketPurchase')

    def __str__(self):
        return f'{self.user.username} Profile'

class TicketPurchase(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    purchase_date = models.DateField(auto_now_add=True)





