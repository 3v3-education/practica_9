from django.shortcuts import get_object_or_404, redirect, render
from .models import Publicacion
from django.http import HttpResponse

#VISTA DEL INICIO EN LA RAIZ / 
def inicio(request):
    return render(request, 'publicaciones/inicio.html')

#READ : Listar publicaciones
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    contexto = {"publicaciones": publicaciones}
    return render(request,"publicaciones/lista_publicaciones.html", contexto)

def detalle_publicacion(request,id):
    publicacion = get_object_or_404(Publicacion,id=id)

    return render(request,"publicaciones/detalle_publicacion.html",{"publicacion":publicacion})

#CREATE : Crear publicaciones

def crear_publicacion(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        descripcion = request.POST["descripcion"]
        autor = request.POST["autor"]
        estado = request.POST["estado"]

        Publicacion.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            autor=autor,
            estado=estado
        )
        return redirect("lista_publicaciones")
    return render(request,"publicaciones/crear_publicacion.html")

#UPDATE: Actualizar una publicacion

def editar_publicacion(request,id):
    publicacion = get_object_or_404(Publicacion,id=id)
    if request.method == "POST":
        publicacion.titulo= request.POST["titulo"]
        publicacion.descripcion = request.POST["descripcion"]
        publicacion.autor = request.POST["autor"]
        publicacion.estado = request.POST["estado"]

        publicacion.save()
        return redirect("lista_publicaciones")
    
    return render(request,"publicaciones/editar_publicacion.html",{"publicacion":publicacion})

#DELETE: Eliminar una publicacion

def eliminar_publicacion(request,id):
    publicacion = get_object_or_404(Publicacion,id=id)
    if request.method == "POST":
        publicacion.delete()
    return redirect("lista_publicaciones")


#FROM publicaciones SELECT * 
# Publicacion.objects.all()
#CRUD - Create Read Updete Delete