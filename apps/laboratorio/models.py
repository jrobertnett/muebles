from django.db import models

# Create your models here.
class Laboratorio(models.Model):
	codigo = models.CharField(max_length=10)
	nombre = models.CharField(max_length=40)
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre
#agregar direccion
