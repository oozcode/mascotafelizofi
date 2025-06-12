from django.urls import path,include
from .import views



urlpatterns = [
    path('',views.index,name='index'),
    path('footer/', views.footer, name='footer'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('veterinaria/', views.veterinaria, name='veterinaria'),
    path('estetica/',views.estetica, name='estetica'),
    path('movil/', views.movil, name='movil'),
]