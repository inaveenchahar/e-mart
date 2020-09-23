from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import login, logout
from django.contrib import messages
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            new_user = User.objects.create_user(
                first_name=instance.first_name,
                last_name=instance.last_name,
                username=instance.username,
                email=instance.email,
                password=instance.password
            )
            login(request, new_user)
            messages.success(request, 'You have successfully signed up as {name}.'.format(name=new_user.username))
            return redirect('main:homepage')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.error(request, 'You are logged out now.')
        return redirect('main:homepage')
    else:
        return redirect('main:homepage')

