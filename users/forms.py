from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms


# Model Forms
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["user", "is_complete"]


# Other Forms
class LoginForm(forms.Form):
    username = forms.CharField(label="Enter Username", max_length=150)
    password = forms.CharField(
        label="Entert Password", max_length=150, widget=forms.PasswordInput()
    )
