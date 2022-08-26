# Register your models here.
from django.contrib import admin

from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("owner_name", "registration_number", "fuel_type", "fitness_upto")
    list_filter = ("fuel_type",)
