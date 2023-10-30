# accounts/urls.py
from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('password_reset/', views.custom_password_reset, name='password_reset'),
    path('password_reset/done/', views.custom_password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.custom_password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.custom_password_reset_complete, name='password_reset_complete'),
]
