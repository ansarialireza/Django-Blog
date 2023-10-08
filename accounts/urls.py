# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),  # URL for user registration
    path('login/', views.login_view, name='login'),    # URL for user login
    path('logout/', views.logout_view, name='logout'),    # URL for user login
    # Add other authentication-related URLs as needed
]
