from django.forms import ModelForm
from django import forms
from .models import *
from customer.models import *


class CreateFoodForm(ModelForm):
    class Meta:
        model = food
        fields = '__all__'
        exclude = ['user']


class CreateBlog(ModelForm):
    class Meta:
        model = blog
        fields = '__all__'
        exclude = ['user']


class CreateFeedback(ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'
        exclude = ['user', 'reservation']
