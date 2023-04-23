
from django.urls import path
from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    #     url adress  views
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('elements', elements, name='elements'),
    path('test', test_view, name='test')

]
