from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import candidateLoginForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Article
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def welcomePage(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/blogs")
    else:
        return render(request, "Home.html", {})

def loginForm(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/blogs")
    else:
        form = candidateLoginForm()
        return render(request, "Login.html", {'form': form, 'status': 1})

def registerForm(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/blogs")
    else:
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
            return HttpResponseRedirect(url)
        else:
            form = candidateLoginForm()
            return render(request, "Login.html", {'form': form, 'status':0})

@login_required(login_url='/login')
def Clogout(request):
    logout(request)
    return HttpResponseRedirect("/login")


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():  # invoke .is_valid
            username = form.cleaned_data['username']
            alreadyUser = User.objects.filter(username=username)
                # print(alreadyUser.count())
            if (alreadyUser.count() != 0):
                form = RegistrationForm()
                return render(request, "Register.html", {'form': form, 'status':0})
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
                return render(request, "Login.html", {'form': form, 'status':1})
        else:
            return HttpResponse("Form is invalid")

@login_required(login_url='/login')
def allBlogs(request):
    listOfArticle = Article.objects.all().order_by("-Date")
    return render(request, "ArticleList.html", {"ArticleList": listOfArticle})

@login_required(login_url='/login')
def addArticle(request):
    return render(request, "addArticle.html")

@login_required(login_url='/login')
def saveArticle(request):
    try:
        print("hello")
        print("Image: ", request.POST['image'])
        article = Article.objects.create(
            title = request.POST['title'],
            author = request.POST['author'],
            Date = request.POST['date'],
            Image = request.POST['image'],
            Content = request.POST['content']
        )
        return HttpResponse("/blogs")
    except:
        return HttpResponse(0)

@login_required(login_url='/login')
def aboutArticle(request, id):
    article = Article.objects.get(id=id)
    user = request.user.username
    return render(request, 'Article.html', {'article':article, 'user':user})
