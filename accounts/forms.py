from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'style': 'font-size:14px;',
    }), label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'style': 'font-size:14px;',
    }), label='Last Name')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'style': 'font-size:14px;',
    }), label='Username')
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'style': 'font-size:14px;',
    }), label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'style': 'font-size:14px;',
    }), label='Password')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']