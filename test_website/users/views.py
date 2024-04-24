from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login_page'))
        else:
            errors = form.non_field_errors()
            return render(request, 'users/register.html', {'form': form, 'errors': errors})
    form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('start_page'))
        else:
            errors = form.non_field_errors()
            return render(request, 'users/login.html', {'form': form, 'errors': errors})
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('start_page'))