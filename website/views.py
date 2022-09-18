from django.shortcuts import render
from django.views import generic, View

# Create your views here.
def index(request):
    return render(request, 'index.html')

def menus(request):
    return render(request, 'menus.html')    

def food_menu(request):
    return render(request, 'food_menu.html')  

def drinks_menu(request):
    return render(request, 'drinks_menu.html')  

def reservations(request):
    return render(request, 'reservations.html')     
