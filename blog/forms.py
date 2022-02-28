from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms import TextInput, Select, MultipleChoiceField


# Login
class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control form'})),
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form'})),


# Register
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'input form', 'autocomplete': 'off'})),
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form input'})),
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form input'})),


# other add blog
class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-c ontrol'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'password1': forms.TextInput(attrs={'class': 'form-control'}),
        'password2': forms.TextInput(attrs={'class': 'form-control'}),
    }


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'content', 'tag', 'category', 'slug', 'photo', ]

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form  col-md-2', 'placeholder': "Title", 'style': 'max-width: 100%;'}),
            'author': forms.TextInput(
                attrs={'class': 'form  col-md-2', 'placeholder': "Author", 'style': 'max-width: 100%;'}),
            'slug': forms.TextInput(
                attrs={'class': 'form col-md-2', 'placeholder': "Url", 'style': 'max-width: 100%;'}),
            'category': forms.Select(attrs={'class': 'form col-md-2', 'style': 'max-width: 100%;'}),
            'content': forms.Textarea(
                attrs={'class': 'form col-md-2 textarea', 'placeholder': "Content", 'style': 'max-width: 100%;'}),
            'tag': forms.SelectMultiple(
                attrs={'class': 'form col-md-2 select select--multiple', 'placeholder': "Content",
                       'style': 'max-width: 100%;'}),
        }
