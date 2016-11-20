from django.db import models

# Create your models here.
class Cliente(models.Model):
	dni = models.IntegerField(primary_key = True)
	nombre = models.CharField(max_length = 50, help_text=("Ingrese el Nombre"))
	apellido = models.CharField(max_length= 70)
	domicilio = models.TextField()


	def __str__(self):
		return '{}{}{}'.format(self.nombre, self.apellido, self.domicilio)