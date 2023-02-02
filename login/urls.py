from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
    path('signupcompany/', views.signupcompany, name='signupcompany'),
    path('', views.index, name='index'),
    path('logincompany/', views.logincompany, name='logincompany'),
    path('signupcustomer/', views.signupcustomer, name='signupcustomer'),
    path('logincustomer/', views.logincustomer, name='logincustomer'),
    path('afterlogincompany/', views.afterlogincompany, name='afterlogincompany'),
    path('afterlogincustomer/', views.afterlogincustomer,
         name='afterlogincustomer'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.index, name='index'),




]
