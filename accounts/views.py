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
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'You have successfully registered and logged in.')
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
    return redirect('/login') 

def home_view(request):
    return render(request, 'website/index.html')


