from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    mobile = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'email', 'mobile', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class BioForm(ModelForm):
    class Meta:
        model = ProfileForm
        fields = "__all__"


class AluForm(ModelForm):
    class Meta:
        model = ExperienceDetails
        fields = "__all__"


class ApplyForm(forms.Form):
    is_applied = forms.BooleanField()


class RegForm(ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
