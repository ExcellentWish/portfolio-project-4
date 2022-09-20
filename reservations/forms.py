from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import Customer, Reservations
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('full_name', 'email', 'phone_number')

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ('no_of_guests', 'requested_time')
        widgets = {
            'requested_time':DateTimePickerInput()
        }
        def get_form(self):
            form = super().get_form()
            form.fields['requested_time'].widget = DateTimePickerInput()
            return form
