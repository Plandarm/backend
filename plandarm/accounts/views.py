from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Profile
from .forms import RegistrationForm
from .decorators import logged_out

def rootRedirect(request):
    return redirect('login')

@logged_out
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            profile = Profile.objects.get(user=user)
            page_id = profile.page_set.first().id
            login(request, user)

            return redirect('/page/' + str(page_id))
        else:
            messages.info(request, 'Incorrect login data')

    return render(request, 'accounts/login-page.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@logged_out
def registerPage(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/reg-page.html', context)
