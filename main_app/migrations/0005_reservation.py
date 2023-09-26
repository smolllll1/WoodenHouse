# Generated by Django 4.2 on 2023-04-06 17:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0004_agents"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
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
                ("name", models.CharField(max_length=100)),
                (
                    "email",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="xxxxxx@xxxxxx",
                                regex="^\\w+(_?\\w*)*-?\\w*(_?\\w*)*@\\w+(\\.\\w*)+$",
                            )
                        ],
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=16,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="the number should have the following format: +380xx xxx xx xx",
                                regex="^\\+?3?8?0?\\d{2}[ -]?(\\d[ -]?){7}$",
                            )
                        ],
                    ),
                ),
                ("date_request", models.DateTimeField(auto_now_add=True)),
                ("date_response", models.DateTimeField(auto_now=True)),
                ("message", models.TextField(blank=True, max_length=1000)),
                ("is_processed", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ("-date_response",),
            },
        ),
    ]