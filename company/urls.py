from django.urls import path
from company import views

app_name = 'company'

urlpatterns = [
    path('addfood/', views.addfood, name='addfood'),
    path('addfeedback/<str:id>/', views.addfeedback, name='addfeedback'),
    path('addblog/', views.addblog, name='addblog'),
    path('showblog/', views.showblog, name='showblog'),
    path('showfood/', views.showfood, name='showfood'),
    path('getresponse/', views.getresponse, name='getresponse'),
    # path('afterlogincustomer/', views.afterlogincustomer,name='afterlogincustomer'),
    # path('logout/', views.logout_user, name='logout'),





]
