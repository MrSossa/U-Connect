from cProfile import label
from socket import fromshare
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class routesForms(forms.Form):
    description = forms.CharField(max_length=300)
    petfriendly = forms.BooleanField()
    route = forms.JSONField(widget = forms.HiddenInput())

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']