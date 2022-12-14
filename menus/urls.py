from menus import views
from django.urls import path, include
from django.conf.urls import include, url


urlpatterns = [
    path('', views.menus, name='menus'),
    path('food_menu/', views.FoodMenu.as_view(), name='food_menu'),
    path('drinks_menu/', views.DrinkMenu.as_view(), name='drinks_menu'),
]
