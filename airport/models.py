from django.db import models
# Create your models here.

class Schedule(models.Model):
    flight_number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    origin = models.CharField(max_length=100)
    departure_time = models.TimeField()
    estimated_departure = models.TimeField(null=True, blank=True)
    arrival_time = models.TimeField()
    estimated_arrival = models.TimeField(null=True, blank=True)
    day = models.DateField()
