from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'index.html')

def footer(request):
    return render(request,'footer.html')

def nosotros(request):
    return render(request,'nosotros.html')

def contacto(request):
    return render(request,'contacto.html')

def veterinaria(request):
    return render(request,'veterinaria.html')

def estetica(request):
    return render(request,'estetica.html')

def movil(request):
    return render(request,'movil.html')