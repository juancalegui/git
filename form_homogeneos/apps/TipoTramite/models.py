from django.db import models
from apps.Tramite.models import Tramite

class TipoTramite(models.Model):
	id_tipo_tramite = models.AutoField(primary_key=True)
	tipo_tramite = models.CharField(max_length=50, blank=True, null=True)
	tramite = models.ForeignKey(Tramite, null=True, blank=True, on_delete= models.CASCADE)
	
	def __str__(self):
		return '{}'.format(self.tipo_tramite)


# Create your models here.
