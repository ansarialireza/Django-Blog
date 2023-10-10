# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in.')
        return redirect('/')  # Redirect to the home page or dashboard

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user object
            user = form.save()
            
            # Get the email from the form separately and save it to the user
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
        # User is already logged in, redirect to the home page or dashboard
        messages.success(request, 'You are logged in')
        return redirect('/')  # Replace 'home' with the URL name of your desired destination

    if request.method == 'POST': 
        # Handle login form submission
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        
        # Try to authenticate with both username and email
        user = authenticate(request, username=username_or_email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the home page or dashboard upon successful login
        else:
            # Handle invalid login credentials here, e.g., display an error message
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('/login')  # Redirect to the login page after logout

def home_view(request):
    return render(request, 'website/index.html')



from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm  # Import your custom form

# class CustomPasswordResetView(PasswordResetView):
#     form_class = CustomPasswordResetForm  # S