from django.shortcuts import render
from django.views import generic, View
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    # Return homepage
    return render(request, 'index.html')

def menus(request):
    return render(request, 'menus.html')    

def food_menu(request):
    return render(request, 'food_menu.html')  

def drinks_menu(request):
    return render(request, 'drinks_menu.html')  

def reservations(request):
    return render(request, 'reservations.html') 

def send_message(request, contact_form):
    customer_name = contact_form.cleaned_data['name']
    subject = (f'Message from {customer_name}')
    message = contact_form.cleaned_data['message']
    email_from = contact_form.cleaned_data['email']
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail( subject, message, email_from, recipient_list )        

class ContactPage(View):
    """
    Contact page - for a user to send a contact form.
    """

    def get(self, request, *args, **kwargs):
        contact_form = ContactForm()
        template = 'contact_us.html'
        if request.user.is_authenticated:
            # if user is logged in pre-populate the fields
            contact_form = ContactForm(initial={'name': request.user.first_name + " " + request.user.last_name, 'email': request.user.email})
        else:
            contact_form = ContactForm()
        return render(request, 'contact_us.html', {'contact_form': contact_form})


    def post(self, request, User=User, *args, **kwargs):

        if request.method == 'POST':
            contact_form = ContactForm(request.POST)

            if form.is_valid():
                # Return blank form so the same message isn't posted twice.
                send_message(request, contact_form)
                contact_form = ContactForm()
                messages.add_message(
                    request, messages.SUCCESS, "Thank you for contacting us, one of our staff will be in touch shortly. <br>For anything urgent please call on +39 329 277 0444"
                )
                return render(request, 'contact_us.html', {'contact_form': contact_form})

            else:
                contact_form = ContactForm(request.POST)
                messages.add_message(
                request, messages.ERROR, "Something is not right with your form - please make sure your email address is entered in the correct format.")

            return render(request, 'contact_us.html', {'contact_form': contact_form})


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)

