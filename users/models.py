from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Flight(models.Model):
    flight_number = models.CharField(max_length=64, unique=True)
    departure_date = models.DateField()
    arrival_date = models.DateField()

class Ticket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE)
    departure_date = models.DateField()
    arrival_date = models.DateField()

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket, through='TicketPurchase')

    def __str__(self):
        return f'{self.user.username} Profile'

class TicketPurchase(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    purchase_date = models.DateField(auto_now_add=True)





