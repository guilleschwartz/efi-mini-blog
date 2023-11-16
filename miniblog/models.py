from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    categorias = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo

