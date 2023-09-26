from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class ProductCutegory(models.Model):
    title = models.CharField(max_length=100, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __iter__(self):
        for i in self.products.all():
            yield i

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        ordering = ("position",)


class Products(models.Model):
    title = models.CharField(max_length=100, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    is_cpecial = models.BooleanField(default=True)
    is_signature = models.BooleanField(default=True)
    categories = models.ForeignKey(ProductCutegory, on_delete=models.CASCADE, related_name="products")
    disc = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    width = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="products")

    def total_price(self):
        return self.price - self.discount / 100 * self.price

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        ordering = ("position",)


class Agents(models.Model):
    title = models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    disc = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to="products")

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        ordering = ("position",)


class Reservation(models.Model):
    phone_validator = RegexValidator(
        regex="^\+?3?8?0?\d{2}[ -]?(\d[ -]?){7}$",
        message="the number should have the following format: +380xx xxx xx xx",
    )
    email_validator = RegexValidator(regex="^\w+(_?\w*)*-?\w*(_?\w*)*@\w+(\.\w*)+$", message="xxxxxx@xxxxxx")
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, validators=(email_validator,))
    phone = models.CharField(max_length=16, validators=(phone_validator,))
    date_request = models.DateTimeField(auto_now_add=True)
    date_response = models.DateTimeField(auto_now=True)
    message = models.TextField(max_length=1000, blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ("-date_response",)

    def __str__(self):
        return f"{self.name}\t{self.phone}\t{self.email}"


class New(models.Model):
    title = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to="dishes")
    is_visible = models.BooleanField(default=True)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("date",)
