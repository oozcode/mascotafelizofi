from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Mascota, Reserva, FichaMedica

class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'is_cliente', 'is_veterinario',  # <-- aquí tus campos personalizados
                'groups', 'user_permissions'
            ),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Roles', {'fields': ('is_cliente', 'is_veterinario')}),
    )
    list_display = UserAdmin.list_display + ('is_cliente', 'is_veterinario')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Mascota)
admin.site.register(Reserva)
admin.site.register(FichaMedica)