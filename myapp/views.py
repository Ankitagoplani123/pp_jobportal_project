
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login as auth_login
from .forms import *
from .models import *


def homepage(request):
    return render(request=request,
                  template_name='main/home.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged In ')
                return redirect('/')
            else:
            messages.add_message(request, messages.INFO, 'Invalid username or password.')
        else:
            messages.add_message(request, messages.INFO, 'Invalid username or password.')
    form = LoginForm()
    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


