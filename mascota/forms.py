from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from.models import Reserva, Mascota, FichaMedica

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        model = Usuario
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Correo",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'autofocus': True
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )

class AgendarForm(forms.Form):
    nombre_mascota = forms.CharField(label="Nombre de la mascota", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo = forms.CharField(label="Tipo de animal", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Perro, Gato'}))
    edad = forms.IntegerField(label="Edad de la mascota", min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    genero = forms.ChoiceField(label="Género", choices=[('macho', 'Macho'), ('hembra', 'Hembra')], widget=forms.Select(attrs={'class': 'form-select'}))
    rut_dueño = forms.CharField(label="RUT del dueño", max_length=12, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12.345.678-9'}))
    tipo_atencion = forms.ChoiceField(
        label="Tipo de atención",
        choices=[('veterinaria','Veterinaria'),('estetica','Estética'),('movil','Veterinaria Móvil')],
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'tipo_atencion'})
    )
    direccion = forms.CharField(label="Dirección", max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'direccion'}))
    fecha_hora = forms.DateTimeField(label="Fecha y hora", widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))

class FichaMedicaForm(forms.ModelForm):
    class Meta:
        model = FichaMedica
        fields = ['procedimiento', 'tratamiento', 'observaciones']
        widgets = {
            'procedimiento': forms.Textarea(attrs={'class': 'form-control'}),
            'tratamiento': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
        }