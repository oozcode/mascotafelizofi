from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = Usuario
        fields = ("email", "password1", "password2")

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Correo electrónico")