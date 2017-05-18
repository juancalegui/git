from django.db import models
from apps.Persona.models import Persona
from apps.Tramite.models import Tramite
from apps.TipoTramite.models import TipoTramite
from django.utils import timezone

class SolicitudTramite(models.Model):
	id_solicitud = models.AutoField(primary_key=True)
	fecha_creacion = models.DateField()
	perso_cuil = models.ForeignKey(Persona, null=True, blank=True, on_delete= models.CASCADE)
	tramite = models.ForeignKey(Tramite, null=True, blank=True, on_delete= models.CASCADE)
	tipo_tramite = models.ForeignKey(TipoTramite, null=True, blank=True, on_delete= models.CASCADE)
	fecha_solicitada = models.DateField()
	cant_dias = models.IntegerField() 
	motivo = models.TextField()
	documentacion = models.CharField(max_length=50, blank=True, null=True)


	def __str__(self):
		return '{}{}'.format(self.id_solicitud,self.perso_cuil)
# Create your models here.
