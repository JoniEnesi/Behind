from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class register_form(UserCreationForm):
    fullname = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'register_place'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'register_place'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'register_place'}))

    class Meta:
        model = User
        fields = ['fullname', 'username', 'password1', 'password2', 'email']


class login_form(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'box_input'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'box_input'}))