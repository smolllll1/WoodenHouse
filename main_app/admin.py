from django.contrib import admin
from .models import ProductCutegory, Products, Agents, Reservation, New

# Register your models here.

# admin.site.register(ProductCutegory)
# admin.site.register(Products)
# admin.site.register(Reservation)
admin.site.register(Agents)


@admin.register(Products)
class DishAdmin(admin.ModelAdmin):
	list_display = ['title', 'position', 'is_visible', 'categories', 'is_cpecial', 'is_signature', 'price', 'discount', 'photo']
	list_filter = ['is_visible', 'is_cpecial', 'is_signature', 'categories']
	list_editable = ['position', 'is_visible', 'categories', 'is_cpecial', 'is_signature', 'price', 'discount', 'photo']

class ProductInline(admin.TabularInline):
	model = Products

@admin.register(ProductCutegory)
class CategoryWithProductsAdmin(admin.ModelAdmin):
	list_display = ['title', 'position', 'is_visible']
	list_filter = ['is_visible']
	list_editable = ['position', 'is_visible']
	inlines = [ProductInline]

@admin.register(Reservation)
class Reservat(admin.ModelAdmin):
	list_display = ['name', 'email', 'date_request', 'phone', 'is_processed']
	list_filter = ['is_processed', 'date_request', 'name', ]
	list_editable = ['phone', 'is_processed']

@admin.register(New)
class New(admin.ModelAdmin):
	list_display = ['title', 'photo', 'date', 'message']
	list_filter = ['date', 'title', ]
	list_editable = ['date']