from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from menus.views import menus, FoodMenu, DrinkMenu

# Create your tests here
class TestUrls(SimpleTestCase):
    def test_menus_url_is_resolved(self):
        url = reverse('menus')
        self.assertEquals(resolve(url).func.__name__, menus.__name__)

    def test_food_menu_url_is_resolved(self):
        url = reverse('food_menu')
        self.assertEquals(resolve(url).func.view_class, FoodMenu)

    def test_drinks_menu_url_is_resolved(self):
        url = reverse('drinks_menu')
        self.assertEquals(resolve(url).func.view_class, DrinkMenu)
