from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    username = forms.CharField(
        help_text="",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your username"
        })
    )

    password1 = forms.CharField(
        help_text="",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Create a password"
        })
    )

    password2 = forms.CharField(
        help_text="",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirm your password"
        })
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]