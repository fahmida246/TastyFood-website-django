from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
from .models import User


class SignUpAdminForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)
    is_admin = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2', 'is_admin')


class SignUpCustomerForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)

    is_customer = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email',  'password1',
                  'password2', 'is_customer')
