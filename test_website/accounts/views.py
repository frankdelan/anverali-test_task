from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accounts.forms import EditExecutorForm, EditCustomerForm


# Create your views here.

def start(request):
    return render(request, 'accounts/index.html')


@login_required(login_url='users:login_page')
def show_profile(request):
    return render(request, 'accounts/profile.html')


@login_required(login_url='users:login_page')
def edit_profile(request):
    if request.method == 'POST':
        if request.user.is_customer:
            form = EditCustomerForm(request.POST, instance=request.user)
        else:
            form = EditExecutorForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:account_page'))
    if request.user.is_customer:
        form = EditCustomerForm(instance=request.user)
    else:
        form = EditExecutorForm(instance=request.user)
    return render(request, 'accounts/edit.html', {'form': form})
