from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.welcomePage, name="welcomePage"),
    url(r'^login', views.loginForm, name="login"),
    url(r'^register', views.registerForm, name="register"),
    url(r'^registration', views.registration, name="registration"),
    url(r'^doLogin', views.Login, name="Login"),
    url(r'^logout', views.Clogout, name='Clogout'),
    url(r'^blog', views.allBlogs, name="allBlogs"),
    url(r'^addArticle', views.addArticle, name='addArticle')

]