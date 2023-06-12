from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class AddOwn(forms.Form):
    name = forms.CharField(label="Name")
    tour = forms.IntegerField(label="Name of tour")
    date = forms.CharField(label="Date")
    phone = forms.IntegerField(label="Phone number")
    address = forms.CharField(label="Address")
