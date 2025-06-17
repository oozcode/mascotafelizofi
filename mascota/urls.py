from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('footer/', views.footer, name='footer'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('veterinaria/', views.veterinaria, name='veterinaria'),
    path('estetica/', views.estetica, name='estetica'),
    path('movil/', views.movil, name='movil'),
    path('agendar/', views.agendar, name='agendar'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil_cliente, name='perfil_cliente'),
    path('dashboard/', views.dashboard_veterinario, name='dashboard_veterinario'),
    path('login/', auth_views.LoginView.as_view(
      template_name='login.html',
      authentication_form=LoginForm
    ), name='login'),
    path('ficha/crear/<int:reserva_id>/', views.crear_ficha, name='crear_ficha'),
    path('ficha/ver/<int:ficha_id>/', views.ver_ficha, name='ver_ficha'),
    path('reserva/aceptar/<int:reserva_id>/', views.aceptar_reserva, name='aceptar_reserva'),
]