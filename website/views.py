from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home (request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been succesfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Authentification failed, please try again")
            return render(request, 'login_user.html', {})
    else:
        return render(request, 'login_user.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return render(request, 'login_user.html', {})

def register_user(request):
    return render(request, "register.html", {})

