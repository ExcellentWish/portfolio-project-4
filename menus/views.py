from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import FoodItems, DrinkItems

# Create your views here.
def menus(request):
    return render(request, 'menus.html')

class FoodMenu(generic.ListView):
    model = FoodItems
    template_name = 'food_menu.html'
    context_object_name = 'food_items'

    def get_queryset(self):
        queryset = {
            'lunch_items': FoodItems.objects.all().filter(on_menu=True, food_menu_section=0),
            'dinner_items': FoodItems.objects.all().filter(on_menu=True, food_menu_section=1)
        }
        return queryset

class DrinkMenu(generic.ListView):
    model = DrinkItems
    template_name = 'drinks_menu.html'
    context_object_name = 'drinks_items'

    def get_queryset(self):
        queryset = {
            'wine_items': DrinkItems.objects.all().filter(on_menu=True, drinks_menu_section=0),
            'water_softdrinks_items': DrinkItems.objects.all().filter(on_menu=True, drinks_menu_section=1),
            'apéritif_items': DrinkItems.objects.all().filter(on_menu=True, drinks_menu_section=2)
        }
        return queryset