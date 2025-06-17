from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Reserva, FichaMedica,Mascota,Animal
from .forms import RegistroForm  
from django.contrib.auth import authenticate, login
from .forms import LoginForm,AgendarForm


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

@login_required(login_url='/login/')
def agendar(request):
    if request.method == 'POST':
        form = AgendarForm(request.POST)
        if form.is_valid():
            # Crear o buscar la mascota
            mascota, _ = Mascota.objects.get_or_create(
                nombre=form.cleaned_data['nombre_mascota'],
                tipo=form.cleaned_data['tipo'],
                edad=form.cleaned_data['edad'],
                dueño=request.user
            )
            # Crear la reserva
            Reserva.objects.create(
                cliente=request.user,
                mascota=mascota,
                tipo_atencion=form.cleaned_data['tipo_atencion'],
                fecha_hora=form.cleaned_data['fecha_hora'],
                direccion=form.cleaned_data['direccion'] if form.cleaned_data['tipo_atencion'] == 'movil' else '',
            )
            return redirect('perfil_cliente')
    else:
        form = AgendarForm()
    return render(request, 'agendar.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']  # Opcional: usa email como username
            user.is_cliente = True
            user.save()
            return redirect('login')
    else:
        form = RegistroForm()
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

@login_required
@user_passes_test(lambda u: u.is_veterinario)
def aceptar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == 'POST':
        reserva.estado = 'aceptado'
        reserva.save()
    return redirect('dashboard_veterinario')

@login_required
@user_passes_test(lambda u: u.is_veterinario)
def ver_ficha(request, ficha_id):
    ficha = get_object_or_404(FichaMedica, id=ficha_id)
    return render(request, 'ver_ficha.html', {'ficha': ficha})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Cambia 'index' por la ruta que prefieras
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


