from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password')
            user = User.objects.create_user('username', (username, raw_passwd))
            login(request, user)
        return redirect('/home/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})