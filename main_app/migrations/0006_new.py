# Generated by Django 4.2 on 2023-04-10 19:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0005_reservation"),
    ]

    operations = [
        migrations.CreateModel(
            name="New",
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
                ("title", models.CharField(max_length=100, unique=True)),
                ("photo", models.ImageField(upload_to="dishes")),
                ("is_visible", models.BooleanField(default=True)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("message", models.TextField(blank=True, max_length=1000)),
            ],
            options={
                "ordering": ("date",),
            },
        ),
    ]