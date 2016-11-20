from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from apps.pago.forms import PagoForm
from apps.pago.models import Pago 
from datetime import datetime, date, time, timedelta

class PagoList(ListView):
	context_object_name = 'pago'
	model = Pago
	template_name ='pago/pago_list.html' 
	paginate_by = 15	
	
	def get_queryset(self):
		hoy = date.today()	
		segundomes= hoy + timedelta(days=30)
		queryset = super(PagoList, self).get_queryset()

		return queryset.filter(fecha_pago__year__gte = hoy.year)	


	
class PagoCreate(CreateView):
	model = Pago
	form_class = PagoForm
	template_name ='pago/pago_form.html'
	success_url = reverse_lazy('pago:pago_listar')

class PagoUpdate(UpdateView):
	model = Pago
	form_class = PagoForm
	template_name ='pago/pago_form.html'
	success_url = reverse_lazy('pago:pago_listar')

class PagoDelete(DeleteView):
	model = Pago
	form_class = PagoForm
	template_name ='pago/pago_delete.html'
	success_url = reverse_lazy('pago:pago_listar')

class PagoCliente(ListView):
	context_object_name = 'pago'
	model = Pago
	template_name ='pago/pago_cliente.html' 
		
	
	def get_queryset(self):
		hoy = date.today()	
		segundomes= hoy + timedelta(days=30)
		queryset = super(PagoCliente, self).get_queryset()

		return queryset.filter(fecha_pago__year__gte = hoy.year)		

	

