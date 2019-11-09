from django.db import models
from apps.adopciones.models import Persona

class Aportacion(models.Model):
     Tipo_ayuda = models.CharField(max_length=50)

     def __str__(self):
         return '{}'.format(self.Tipo_ayuda)


class Ninio(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    fecha_nac = models.DateField(blank=True)
    edad = models.IntegerField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    aportacion = models.ManyToManyField(Aportacion,blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)
