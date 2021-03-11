from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

from photoshare import utils
from users.forms import SignUpForm


# Create your views here.
@utils.anonymous_required
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return HttpResponseRedirect(reverse('index'))

        return render(request, 'users/signup.html', {'form': form})
        
    return render(request, 'users/signup.html', {'form': SignUpForm()})


@utils.anonymous_required
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return HttpResponseRedirect(reverse('index'))

        return render(request, 'users/login.html', {'form': form})


    return render(request, 'users/login.html', {'form': AuthenticationForm()})

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


















