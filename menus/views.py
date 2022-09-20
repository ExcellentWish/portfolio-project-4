from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import FoodItem, DrinkItem

# Create your views here.
def menus(request):
    return render(request, 'menus.html')

class FoodMenu(generic.ListView):
    model = FoodItem
    template_name = 'food_menu.html'
    context_object_name = 'food_items'

    def get_queryset(self):
        queryset = {
            'lunch_items': FoodItem.objects.all().filter(on_menu=True, food_menu_section=0),
            'dinner_items': FoodItem.objects.all().filter(on_menu=True, food_menu_section=1)
        }
        return queryset

class DrinkMenu(generic.ListView):
    model = DrinkItem
    template_name = 'drinks_menu.html'
    context_object_name = 'drinks_items'

    def get_queryset(self):
        queryset = {
            'wine_items': DrinkItem.objects.all().filter(on_menu=True, drinks_menu_section=0),
            'water_softdrinks_items': DrinkItem.objects.all().filter(on_menu=True, drinks_menu_section=1),
            'apéritif_items': DrinkItem.objects.all().filter(on_menu=True, drinks_menu_section=2)
        }
        return queryset