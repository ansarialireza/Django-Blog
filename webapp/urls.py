
from django.urls import path
from webapp.views import *

urlpatterns = [
    #     url adress  views
    path('home',home),
    path('about',about),
    path('contact',contact)
    
]