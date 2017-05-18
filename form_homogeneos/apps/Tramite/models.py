from django.db import models

class Tramite(models.Model):

	id_tramite = models.AutoField(primary_key=True)
	tramite = models.CharField(max_length=30)
	
	def __str__(self):
		return '{}'.format(self.tramite)

# Create your models here.
