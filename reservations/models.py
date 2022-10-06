from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from django.contrib.auth.models import User

status_choices = (("pending", "pending"), ("confirmed", "confirmed"))
time_choices = (
    ("12:30", "12:30"),
    ("13:00", "13:00"),
    ("13:30", "13:30"),
    ("14:00", "14:00"),
    ("14:30", "14:30"), 
    ("15:00", "15:00"),
    ("15:30", "15:30"),
    ("19:00", "19:00"),
    ("19:30", "19:30"),
    ("20:00", "20:00"),
    ("20:30", "20:30"),
    ("21:00", "21:00"),
    ("21:30", "21:30"),
    ("22:00", "22:00"),
    ("22:30", "22:30"),
    )

# Create your models here.
class Customer(models.Model):
    """
    Customer information model
    """
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, default="")
    phone_number = PhoneNumberField(null=True)

    # return the full name as this is easier for the admin to read
    def __str__(self):
        return self.full_name
    # def __str__(self):
    #     return str(self.customer_id)

class Table(models.Model):
    """
    Restaurant table model
    """
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=10, default="New table", unique=True)
    max_no_people = models.IntegerField()

    def __str__(self):
        return self.table_name


class Reservation(models.Model):
    """
    Reservation model, which uses information from Customer and Table
    """
    reservation_id = models.AutoField(primary_key=True)
    customer_name  = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer", null=True)
    guests_choices = ((1, "1 person"), (2, "2 people"), (3, "3 people"), (4, "4 people"))
    no_of_guests = models.IntegerField(choices=guests_choices, default=1)
    requested_time = models.DateTimeField()
    requested_date = models.DateField(default=datetime.date.today)
    requested_time = models.CharField(max_length=10, choices=time_choices, default='12:00')
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="table_booked", null=True)
    status_choices = ((0, "pending"), (1, "confirmed"))
    status = models.CharField(
        max_length=10, choices=status_choices, default="pending")

    def __str__(self):
        return str(self.reservation_id)
