from django.urls import path
from customer import views

app_name = 'customer'

urlpatterns = [
    path('getreservation/', views.getreservation, name='getreservation'),
    path('getfeedback/', views.getfeedback, name='getfeedback'),
    path('productshow', views.productshow, name='productshow'),
    # path('showcart/', views.showcart, name='showcart'),
    path('showfav/', views.showfav, name='showfav'),
    path('addtofav/<int:id>/', views.addtofav, name='addtofav'),



]
