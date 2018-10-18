
from django.db import models

class Persona(models.Model):

	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=50)
	email = models.EmailField()
	domicilio = models.CharField(max_length=50)


	def __str__(self):
		return '{} {}'.format(self.nombre, self.apellido)


class Solicitud(models.Model):

	persona = models.ForeignKey(Persona,null=True,blank=True)
	numero_mascotas = models.IntegerField()
	razones = models.TextField()

