from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Puedes agregar más campos si lo necesitas
    is_cliente = models.BooleanField(default=True)
    is_veterinario = models.BooleanField(default=False)

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mascotas')

class Reserva(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    tipo_atencion = models.CharField(max_length=30, choices=[('veterinaria','Veterinaria'),('estetica','Estética'),('movil','Veterinaria Móvil')])
    fecha_hora = models.DateTimeField()
    direccion = models.CharField(max_length=255, blank=True, null=True)  # Solo para movil
    enlace_maps = models.URLField(blank=True, null=True)
    estado = models.CharField(max_length=20, default='pendiente')

class FichaMedica(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='fichas')
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='fichas')
    veterinario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='fichas_realizadas')
    fecha = models.DateTimeField(auto_now_add=True)
    procedimiento = models.TextField()
    tratamiento = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)