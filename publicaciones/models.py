from django.db import models

# Create your models here.

class Publicacion(models.Model):
    ESTADOS = [("borrador","Borrador"),("publicado","Publicado"),("archivado","Archivado")]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="borrador")
    url_imagen = models.URLField( max_length=500, blank=True, null=True)

    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        #return self.titulo
        return f"{self.titulo} - {self.autor}"