from django.contrib import admin
from .models import FoodItems, DrinkItems

# Register your models here.
@admin.register(FoodItems)
class FoodAdmin(admin.ModelAdmin):

    list_filter = ('on_menu', 'updated_on')
    list_display = ('dish_name', 'price','food_menu_section', 'on_menu')


@admin.register(DrinkItems)
class DrinksAdmin(admin.ModelAdmin):

    list_filter = ('on_menu', 'updated_on')
    list_display = ('drink_name', 'price','drinks_menu_section', 'on_menu')
