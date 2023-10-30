# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in.')
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = request.POST['email']
            user = form.save(commit=False)
            user.is_active = False 
            user.save()
            # No login call here, so the user won't be logged in automatically
            messages.success(request, 'You have successfully registered.')
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})



def login_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in.')
        return redirect('/')  
    if request.method == 'POST': 
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        user = authenticate(request, username=username_or_email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful. Welcome !')
            return redirect('/') 
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('/') 

from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm 

def custom_password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Handle the form submission here
            # You can access the submitted data via form.cleaned_data
            # For example, send a custom email or log the request
            # After handling the reset, you can redirect to the password reset done view
            return render(request, 'registration/custom_password_reset_done.html')
    else:
        form = PasswordResetForm()
    
    return render(request, 'registration/custom_password_reset.html', {'form': form})

# Other views for the password reset process
def custom_password_reset_done(request):
    # Customize the password reset done view if needed
    return render(request, 'registration/custom_password_reset_done.html')

def custom_password_reset_confirm(request, uidb64, token):
    # Customize the password reset confirm view if needed
    return render(request, 'registration/custom_password_reset_confirm.html')

def custom_password_reset_complete(request):
    # Customize the password reset complete view if needed
    return render(request, 'registration/custom_password_reset_complete.html')