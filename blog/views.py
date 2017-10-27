from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import candidateLoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def welcomePage(request):
    return render(request, "Home.html", {})

def loginForm(request):
    form = candidateLoginForm()
    return render(request, "Login.html", {'form': form})

def registerForm(request):
    form = RegistrationForm()
    return render(request, "Register.html", {'form': form})

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            url = "/blog"
            return HttpResponse("Login Done")
        else:
            form = candidateLoginForm()
            return render(request, "Login.html", {'form': form})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():  # invoke .is_valid
            username = form.cleaned_data['username']
            alreadyUser = User.objects.filter(username=username)
                # print(alreadyUser.count())
            if (alreadyUser.count() != 0):
                form = RegistrationForm()
                return render(request, "reg.html", {'form': form, "name": name, 'stat': "User already exist"})
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                form = candidateLoginForm()
                return render(request, "Login.html", {'form': form})
        else:
            return HttpResponse("Form is invalid")