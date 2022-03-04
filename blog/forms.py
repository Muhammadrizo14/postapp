from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Login
class UserLoginForm(AuthenticationForm):
    name = forms.CharField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form  col-md-2'})),
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form'})),


# Register
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'input form', 'autocomplete': 'off',
                                                             'placeholder': "Имя пользователя", })),
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form  col-md-2', 'placeholder': "Пароль", })),
    password2 = forms.CharField(label='Повтарите пароль', widget=forms.PasswordInput(
        attrs={'class': 'form  col-md-2', 'placeholder': "Повтарите пароль", })),

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
