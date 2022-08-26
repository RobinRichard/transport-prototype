from django.db import models
from datetime import date


FUEL_CHOICES = [("petrol", "PETROL"), ("diesel", "DIESEL"), ("electric", "ELECTRIC")]


class Registration(models.Model):
    owner_name = models.CharField(max_length=256)
    registration_number = models.CharField(max_length=20)
    model = models.CharField(max_length=256)
    vehicle_class = models.CharField(max_length=256)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES, default="petrol")
    registration_date = models.DateField(default=date.today)
    chassis_number = models.CharField(max_length=100)
    engine_number = models.CharField(max_length=100)
    fitness_upto = models.DateField(default=date.today)
    insurance_expiry = models.DateField(default=date.today)
    registering_authority = models.CharField(max_length=256)

    def __str__(self):
        return self.owner_name

    @property
    def is_fit(self):
        return "GOOD" if date.today() > self.fitness_upto else "BAD"
