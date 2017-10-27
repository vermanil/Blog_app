from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.welcomePage, name="welcomePage"),
    url(r'^login', views.loginForm, name="login"),
    url(r'^register', views.registerForm, name="register")
]
