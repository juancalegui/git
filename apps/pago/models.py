from django.db import models
from apps.cliente.models import Cliente
# Create your models here.
from django.utils import timezone
from datetime import datetime, date, time, timedelta

class Pago(models.Model):
	#fv = datetime.date.today() + timedelta(days = 30)
	cliente = models.ForeignKey(Cliente, null = True, blank = True, on_delete = models.CASCADE)
	fecha_pago = models.DateField(default = timezone.now())
	fecha_vencimiento = models.DateField(default = timezone.now() + timedelta(days=30))
	cantidad = models.DecimalField(max_digits=7, decimal_places=2, default=250.00)
	
	def __str__(self):
		return '{}{}'.format(self.cliente,self.cantidad )


	

def estado(self):
	hoy = datetime.date.today()
	dias = (self.fecha_pago - hoy).days
	return dias