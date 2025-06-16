from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Reserva, FichaMedica

def index(request):
    return render(request, 'index.html')

def footer(request):
    return render(request, 'footer.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contacto(request):
    return render(request, 'contacto.html')

def veterinaria(request):
    return render(request, 'veterinaria.html')

def estetica(request):
    return render(request, 'estetica.html')

def movil(request):
    return render(request, 'movil.html')

def agendar(request):
    return render(request, 'agendar.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_cliente = True  # Si usas tu modelo personalizado
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def perfil_cliente(request):
    reservas = request.user.reservas.select_related('mascota').all()
    return render(request, 'perfil_cliente.html', {'reservas': reservas})

def es_veterinario(user):
    return user.is_authenticated and user.is_veterinario

@login_required
@user_passes_test(es_veterinario)
def dashboard_veterinario(request):
    reservas = Reserva.objects.select_related('mascota', 'cliente').all().order_by('-fecha_hora')
    return render(request, 'dashboard_veterinario.html', {'reservas': reservas})

@login_required
@user_passes_test(es_veterinario)
def crear_ficha(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        procedimiento = request.POST['procedimiento']
        tratamiento = request.POST['tratamiento']
        observaciones = request.POST.get('observaciones', '')
        FichaMedica.objects.create(
            mascota=reserva.mascota,
            reserva=reserva,
            veterinario=request.user,
            procedimiento=procedimiento,
            tratamiento=tratamiento,
            observaciones=observaciones
        )
        return redirect('dashboard_veterinario')
    return render(request, 'crear_ficha.html', {'reserva': reserva})

from .forms import RegistroForm, LoginForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']  # Usa el correo como username
            user.is_cliente = True
            user.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})