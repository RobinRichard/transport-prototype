# Generated by Django 4.1 on 2022-08-26 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("owner_name", models.CharField(max_length=256)),
                ("registration_number", models.CharField(max_length=20)),
                ("model", models.CharField(max_length=256)),
                ("vehicle_class", models.CharField(max_length=256)),
                (
                    "fuel_type",
                    models.CharField(
                        choices=[
                            ("petrol", "PETROL"),
                            ("diesel", "DIESEL"),
                            ("electric", "ELECTRIC"),
                        ],
                        default="petrol",
                        max_length=20,
                    ),
                ),
                ("registration_date", models.DateField(default=datetime.date.today)),
                ("chassis_number", models.CharField(max_length=100)),
                ("engine_number", models.CharField(max_length=100)),
                ("fitness_upto", models.DateField(default=datetime.date.today)),
                ("insurance_expiry", models.DateField(default=datetime.date.today)),
                ("registering_authority", models.CharField(max_length=256)),
            ],
        ),
    ]
