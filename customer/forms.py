from django.forms import ModelForm
from django import forms
from .models import *


class CreateReservation(ModelForm):

    class Meta:
        model = reservation
        fields = '__all__'
        exclude = ['user']
