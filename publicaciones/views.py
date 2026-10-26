from django.shortcuts import get_object_or_404, redirect, render
from .models import Autor, Publicacion
from django.http import HttpResponse

#VISTA DEL INICIO EN LA RAIZ / 
def inicio(request):
    return render(request, 'publicaciones/inicio.html')

#READ : Listar publicaciones
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    busqueda = request.GET.get("buscar")
    if busqueda:
        publicaciones = publicaciones.filter(titulo__icontains = busqueda)
    estado = request.GET.get("estado")
    if estado:
        publicaciones= publicaciones.filter(estado=estado)
    orden = request.GET.get("orden","reciente")
    if orden == "antiguo":
        publicaciones = publicaciones.order_by("fecha_creacion")
    else: 
        publicaciones = publicaciones.order_by("-fecha_creacion")
    contexto = {"publicaciones": publicaciones,"busqueda":busqueda,"estado":estado,"orden":orden}
    return render(request,"publicaciones/lista_publicaciones.html", contexto)

def detalle_publicacion(request,id):
    publicacion = get_object_or_404(Publicacion,id=id)

    return render(request,"publicaciones/detalle_publicacion.html",{"publicacion":publicacion})

def lista_autores(request):
    autores = Autor.objects.all()
    busqueda = request.GET.get("buscar")
    if busqueda:
        autores = autores.filter(username__icontains = busqueda)
    return render(request,"autores/lista_autores.html",{"autores":autores})

def perfil_autor(request,id):
    autor = get_object_or_404(Autor,id=id)
    publicaciones = autor.publicaciones.all()

    return render(request,"autores/perfil_autor.html",{"autor":autor,"publicaciones":publicaciones})

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

def crear_autor(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        email = request.POST["email"]
        username = request.POST["username"]
        autor = Autor(nombre=nombre,apellido=apellido,email=email,username=username)
        autor.save()

        return redirect("inicio")
    return render(request,"autores/crear_autor.html")

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