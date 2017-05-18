from django.db import models

class Persona(models.Model):

	cuil = models.CharField(max_length=14, primary_key=True)
	nombre = models.CharField(max_length=50, blank=True, null=True)
	legajo = models.CharField(max_length=10, blank=True, null=True)
	subrogancia = models.NullBooleanField()
	borrado	= models.NullBooleanField()
    
	def __str__(self):
		return'{}'.format(self.nombre)
	
# Create your models here.
