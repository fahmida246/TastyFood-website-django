from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.


def signupcompany(request):
    form = SignUpAdminForm()
    registered = False
    if request.method == 'POST':
        form = SignUpAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            return render(request, 'login/logincompany.html', locals())

    dict = {'form': form, 'registered': registered}
    return render(request, 'login/signupcompany.html', context=dict)


def signupcustomer(request):
    form = SignUpCustomerForm()
    registered = False
    if request.method == 'POST':
        form = SignUpCustomerForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            return render(request, 'login/logincustomer.html', locals())

    dict = {'form': form, 'registered': registered}
    return render(request, 'login/signupcustomer.html', context=dict)


def logincompany(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)

                return render(request, 'company/afterlogincompany.html', locals())

    return render(request, 'login/logincompany.html', context={'form': form})


def logincustomer(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_customer:
                login(request, user)
                return render(request, 'customer/afterlogincustomer.html', locals())

    return render(request, 'login/logincustomer.html', context={'form': form})


# @login_required
def logout_user(request):
    logout(request)
    return redirect('/')


def afterlogincompany(request):

    return render(request, 'company/afterlogincompany.html')


def afterlogincustomer(request):

    return render(request, 'customer/afterlogincustomer.html')


def index(request):
    return render(request, 'index.html')
