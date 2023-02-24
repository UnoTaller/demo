from django.db import models

# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    receta = models.CharField(max_length=300)
    img = models.ImageField(upload_to='especialidades')

    def __str__(self):
        return self.nombre
