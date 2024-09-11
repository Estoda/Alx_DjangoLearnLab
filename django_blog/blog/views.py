from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomerUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomerUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def profile(request):
    return render(request, 'blog/profile.html')
    
