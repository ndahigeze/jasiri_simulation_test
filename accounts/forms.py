from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import TextInput, Textarea, EmailInput, PasswordInput

from accounts.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserCreateForm(UserCreationForm):
    # genderChoices = (('Male', 'Male'), ('Female', 'Female'))

    # phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'h-form-control phone-international-format'}))

    class Meta:
        model =  User
        fields = ("first_name","last_name","email","username","password1", "password2")
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'username"': TextInput(attrs={'class': 'form-control'}),
            'password1"': PasswordInput(attrs={'class': 'form-control'}),
            'password2"': PasswordInput(attrs={'class': 'form-control'}),
        }


class Meta:
        model = User
        fields = ("first_name","last_name","email","phone","username","password1", "password2")
        widgets = {
            'phone': forms.EmailInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username"': forms.TimeInput(attrs={'class': 'form-control'}),
            'password1"': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2"': forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'username')


class LoginForm(forms.Form):

    class Meta:
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'h-form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'h-form-control'}),
        }


class ChangeUsernameForm(forms.Form):
    username = forms.TextInput()
    password = forms.TextInput()

    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'h-form-control',}),
            'password': forms.PasswordInput(attrs={'class': 'h-form-control'}),
        }






