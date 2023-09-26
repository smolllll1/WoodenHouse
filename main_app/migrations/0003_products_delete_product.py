# Generated by Django 4.1.7 on 2023-03-21 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0002_alter_productcutegory_options_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
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
                ("position", models.PositiveSmallIntegerField()),
                ("is_visible", models.BooleanField(default=True)),
                ("is_cpecial", models.BooleanField(default=True)),
                ("is_signature", models.BooleanField(default=True)),
                ("disc", models.TextField(blank=True, max_length=200)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("discount", models.PositiveSmallIntegerField(default=0)),
                ("width", models.CharField(max_length=100)),
                ("height", models.CharField(max_length=100)),
                ("length", models.CharField(max_length=100)),
                ("photo", models.ImageField(upload_to="products")),
                (
                    "categories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="main_app.productcutegory",
                    ),
                ),
            ],
            options={
                "ordering": ("position",),
            },
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]