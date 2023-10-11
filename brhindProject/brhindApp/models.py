from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    flight_number = models.CharField(max_length=60, null=True, blank=True)
    flight_destinacion = models.CharField(max_length=60, null=True, blank=True)
    flight_destinacion2 = models.CharField(max_length=60, null=True, blank=True)
    country_1 = models.CharField(max_length=60, null=True, blank=True)
    country_2 = models.CharField(max_length=60, null=True, blank=True)
    time = models.CharField(max_length=60, null=True, blank=True)
    time_1 = models.CharField(max_length=60, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 199.99


    def __str__(self):
        return f'{self.flight_destinacion} - {self.time} - {self.time_1}'


class Booking(models.Model):
    travel_id = models.AutoField(primary_key=True)
    travel_roundtrip = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    travel_city = models.CharField(max_length=60, null=True, blank=True)
    travel_departing = models.DateField(max_length=60, null=True, blank=True)
    travel_returing = models.DateField(max_length=60, null=True, blank=True)
    travel_adults = models.IntegerField(null=True, blank=True)
    travel_flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True, blank=True)
    ticket_is_paid = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.travel_id}'

    def total_price(self):
        total_price = self.travel_flight.price * self.travel_adults
        return total_price


class Order (models.Model):
    pass