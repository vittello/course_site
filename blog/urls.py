
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('uslugi', views.service, name='service'),
    path('about', views.contacti, name='contacti') 
]
