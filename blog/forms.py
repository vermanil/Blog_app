from django import forms
# from froala_editor.widgets import FroalaEditor


class candidateLoginForm(forms.Form):
    username = forms.CharField(label="Username", required=True, max_length=30,
                               widget=forms.TextInput(
                                   attrs={'class': 'border-gradient', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", required=True, max_length=30,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'border-gradient', 'name': 'password', 'placeholder': 'Password'}))


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=True, max_length=30, widget=forms.TextInput(
        attrs={'name': 'first_name', 'placeholder': 'First_Name'}))
    last_name = forms.CharField(label='Last Name', required=True,
                                widget=forms.TextInput(attrs={'name': 'last_name', 'placeholder': 'Last_Name'}))
    username = forms.CharField(label='Username', required=True, max_length=30,
                               widget=forms.TextInput(attrs={'name': 'username', 'placeholder': 'UserName'}))
    password = forms.CharField(label='Password', required=True, max_length=30,
                               widget=forms.PasswordInput(attrs={'name': 'password', 'placeholder': 'Password'}))
    email = forms.EmailField(label='Email', required=True,
                             widget=forms.EmailInput(attrs={'name': 'email', 'placeholder': 'Email'}))


# class PageForm(forms.Form):
#     content = forms.CharField(widget=FroalaEditor(options={
#     'toolbarInline': True,
#   }))