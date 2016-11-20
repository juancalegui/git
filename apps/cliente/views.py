from django.shortcuts import render, render_to_response
from apps.cliente.models import Cliente
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from apps.cliente.forms import ClienteForm
from django.db.models import Q
#from listable.views import BaseListableView
# Create your views here.
def index(request):
	return render(request,'cliente/index.html')

class ClienteList(ListView):
	model = Cliente
	template_name ='cliente/cliente_list.html' 
	paginate_by = 5			

class ClienteCreate(CreateView):
	model = Cliente
	form_class = ClienteForm
	template_name ='cliente/cliente_form.html'
	success_url = reverse_lazy('cliente:cliente_listar')

class ClienteUpdate(UpdateView):
	model = Cliente
	form_class = ClienteForm
	template_name ='cliente/cliente_form.html'
	success_url = reverse_lazy('cliente:cliente_listar')

class ClienteDelete(DeleteView):
	model = Cliente
	form_class = ClienteForm
	template_name ='cliente/cliente_delete.html'
	success_url = reverse_lazy('cliente:cliente_listar')


def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) 
            #Q(authors__last_name__icontains=query)
        )
        results = Cliente.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("cliente/search.html", {
        "results": results,
        "query": query
    })

#class ClienteListable(BaseListableView):

#	model = models.Cliente

#	fields =("dni","nombre","apellido","domicilio",)

#	search_fields = {
#		"apellido":("apellido__incontains")
#	}
    		    