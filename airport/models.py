from django.db import models
# Create your models here.

class Schedule(models.Model):
    flight_number = models.CharField(max_length=100, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    estimated_departure = models.TimeField()
    arrival_time = models.TimeField()
    estimated_arrival = models.TimeField()
    day = models.DateField()
    status = models.CharField(max_length=100)
