from django.shortcuts import render, redirect,HttpResponse
from django.http import HttpResponseRedirect
from .forms import ContactForm,NewsletterForm
from django.contrib import messages

def home(request):
    return render(request, 'website/index.html')
def about(request):
    return render(request, 'website/about.html')
def elements(request):
    return render(request, 'website/elements.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to a thank you page or any other appropriate page
            return HttpResponse("Form submitted successfully")
        

    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for subscribing!")
            return HttpResponseRedirect('/')
        else:
            # Handle form errors and add custom messages
            for field, errors in form.errors.items():
                for error in errors:
                    # Add a custom error message to the messages framework
                    messages.add_message(request, messages.ERROR, f"Form error for field {field}: {error}")
    else:
        form = NewsletterForm()

    return HttpResponseRedirect('/')