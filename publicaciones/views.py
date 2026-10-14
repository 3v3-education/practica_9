from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def inicio(request):
    return render(request, 'publicaciones/inicio.html')

def lista_publicaciones(request):
    publicaciones = [
        {"titulo": "mi primer publicacion", "autor":"Ana"},
        {"titulo": "Aprendiendo djangoo!", "autor":"Luis"},
        {"titulo": "Vistas y rutas", "autor":"Marta"}
    ]

    contexto = {"publicaciones": publicaciones}
    return render(request,"publicaciones/lista_publicaciones.html", contexto)