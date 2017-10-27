from django.shortcuts import render
from django.http import HttpResponse
from .forms import candidateLoginForm, RegistrationForm

# Create your views here.

def welcomePage(request):
    return render(request, "Home.html", {})

def loginForm(request):
    form = candidateLoginForm()
    return render(request, "Login.html", {'form': form, 'name':'Anil'})

def registerForm(request):
    form = RegistrationForm()
    return render(request, "Register.html", {'form': form, 'name': 'Anil'})

def registration(request):
    def candidateRegister(request, name):
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
                    return render(request, "Login.html", {'form': form, "name": name})