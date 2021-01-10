from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserAddress


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


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'style': 'font-size:14px',
    }), label='Username', required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'style': 'font-size:14px',
    }), label='Password', required=True)


class UserAddressForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        # 'placeholder': 'Username',
        'style': 'font-size:14px',
    }), label='Full Name', required=True)
    phone_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '10 digit phone number without prefix',
        'style': 'font-size:14px',
    }), label='Phone Number', required=True)
    pincode = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Six digit Pincode',
        'style': 'font-size:14px',
    }), label='Pincode', required=True)
    house_no = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        # 'placeholder': 'House/Flat no. and building name',
        'style': 'font-size:14px',
    }), label='House/Flat no. and building name', required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        # 'placeholder': 'Area, Colony, Street, Sector, Village',
        'style': 'font-size:14px',
    }), label='Area, Colony, Street, Sector, Village', required=True)
    landmark = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Eg. DPS School',
        'style': 'font-size:14px',
    }), label='Landmark', required=True)
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        # 'placeholder': 'Area, Colony, Street, Sector, Village',
        'style': 'font-size:14px',
    }), label='City', required=True)

    class Meta:
        model = UserAddress
        fields = ['full_name', 'phone_no', 'pincode', 'house_no', 'address', 'landmark', 'city']
