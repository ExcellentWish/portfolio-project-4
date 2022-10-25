from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField(label='Your email')
    message = forms.CharField(widget=forms.Textarea)