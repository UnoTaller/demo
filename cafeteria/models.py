from django.db import models

# Create your models here.
class RedSocial(models.Model):
    ico = models.ImageField(upload_to='redes_sociales')
    nombre = models.CharField(max_length=50)
    link = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
class Negocio(models.Model):
    logo = models.ImageField(upload_to='negocio')
    nombre = models.CharField(max_length=50)
    redes = models.ManyToManyField(RedSocial)
    def __str__(self):
        return self.nombre

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    receta = models.CharField(max_length=300)
    img = models.ImageField(upload_to='especialidades')

    def __str__(self):
        return self.nombre
