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
    queryset = DrinkItems.objects.filter(on_menu=True).order_by('drinks_menu_section')
    template_name = 'drinks_menu.html'