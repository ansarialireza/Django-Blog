from django.shortcuts import render, redirect,HttpResponse
from .forms import ContactForm

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

