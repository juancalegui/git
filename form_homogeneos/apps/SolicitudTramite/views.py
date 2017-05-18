from django.shortcuts import render
from django.views.generic import CreateView
from apps.SolicitudTramite.forms import SolicitudTramiteForm
from apps.SolicitudTramite.models import SolicitudTramite
'''class SolicitudTramite(CreateView):
	model = SolicitudTramite
	form_class = ClienteForm
	template_name ='cliente/cliente_form.html'
	success_url = reverse_lazy('cliente:cliente_listar')

# Create your views here.
'''
def index(request):
	return render(request,'solicitudtramite/solicitudtramite.html')

class SolicitudTramiteCreate(CreateView):
	model = SolicitudTramite
	form_class = SolicitudTramiteForm
	template_name ='solicitudtramite/solicitudtramite.html'
	#success_url = reverse_lazy('pago:pago_listar')