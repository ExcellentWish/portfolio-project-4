from django.shortcuts import render
from django.views import generic, View
from .forms import ContactForm
from django.http import HttpResponseRedirect

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

class ContactPage(View):

    def get(self, request, *args, **kwargs):
        contact_form = ContactForm()
        template = 'contact_us.html'
        return render(request, 'contact_us.html', {'contact_form': contact_form})


    def contact_form(request):

        if request.method == 'POST':
            contact_form = ContactForm(request.POST)

            if form.is_valid():
                return render(request, 'contact_us.html', {'contact_form': contact_form})

            else:
                contact_form = ContactForm()

            return render(request, 'contact_us.html', {'contact_form': contact_form})