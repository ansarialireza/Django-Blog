from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User  # You might need to import your custom User model if you're using one

class CustomPasswordResetForm(PasswordResetForm):
    # Add custom fields if needed
    username = forms.CharField(max_length=150, required=True, help_text='Required. Your username.')

    def clean_username(self):
        # Custom validation for the username field
        username = self.cleaned_data['username']
        # You can add your validation logic here
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("This username does not exist.")
        return username

    # You can also override other methods if needed
