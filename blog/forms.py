from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class candidateLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'border-gradient', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'border-gradient', 'name': 'password', 'placeholder': 'Password'}))


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'name': 'first_name', 'placeholder': 'First_Name'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'name': 'last_name', 'placeholder': 'Last_Name'}))
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'name': 'username', 'placeholder': 'UserName'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'name': 'password', 'placeholder': 'Password'}))
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'name': 'email', 'placeholder': 'Email'}))