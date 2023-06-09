from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    detalles = models.TextField()

    def __str__(self):
        return self.nombre

class Comunicado(models.Model):
    NIVELES = (
        ('GEN', 'General'),
        ('PRE', 'Preescolar'),
        ('BAS', 'Básico'),
        ('MED', 'Medio'),
    )

    titulo = models.CharField(max_length=100)
    detalle = models.TextField()
    nivel = models.CharField(max_length=20, choices=NIVELES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo