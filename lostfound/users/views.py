from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            registration_no = form.cleaned_data.get('registration_no')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(registration_no=registration_no, password=raw_password)
            login(request, user)
            messages.success(request, f'Your account has been created successfully!')
            return redirect('posts/')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form}, {'title':'Register'})


def notifications(request):
    return render(request, 'users/notifications.html', {'title':'Notifications'})

