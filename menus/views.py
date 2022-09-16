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
    queryset = FoodItems.objects.filter(on_menu=True).order_by('food_menu_section')
    template_name = 'food_menu.html'

class DrinkMenu(generic.ListView):
    model = DrinkItems
    queryset = DrinkItems.objects.filter(on_menu=True).order_by('drinks_menu_section')
    template_name = 'drinks_menu.html'