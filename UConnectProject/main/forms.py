from cProfile import label
from socket import fromshare
from tkinter import Widget
from django import forms

class routesForms(forms.Form):
    description = forms.CharField(max_length=300)
    petfriendly = forms.BooleanField()
    route = forms.JSONField(widget = forms.HiddenInput())