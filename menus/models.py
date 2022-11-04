from django.db import models

FOOD_MENU_SECTION = ((0, "Lunch"), (1, "Dinner"))
DRINKS_MENU_SECTION = ((0, "Wine")), ((1, "Water/Soft Drinks")), ((2, "Apéritif"))

# Create your models here.
class FoodItem(models.Model):
    """
    Food items model
    """
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    dietary = models.CharField(max_length=200)
    food_menu_section = models.IntegerField(choices=FOOD_MENU_SECTION, default=1)
    allergens = models.CharField(max_length=200)
    on_menu = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-on_menu']

    def __str__(self):
        return self.dish_name


class DrinkItem(models.Model):
    """
    Drink items model
    """
    drink_id = models.AutoField(primary_key=True)
    drink_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    drinks_menu_section = models.IntegerField(choices=DRINKS_MENU_SECTION, default=0)
    on_menu = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-on_menu']

    def __str__(self):
        return self.drink_name
