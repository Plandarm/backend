from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def mainPage(request):
    return render(request, 'accounts/index.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/admin')
        else:
            messages.info(request, 'Incorrect login data')

    return render(request, 'accounts/login-page.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
