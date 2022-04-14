from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    mobile = forms.IntegerField()
    

    class Meta:
        model = User
        fields = ('username',  'email', 'mobile','password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


