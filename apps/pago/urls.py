from django.conf.urls import url
from apps.pago.views import PagoList, PagoCreate, PagoUpdate, PagoDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
	#url(r'^$', index, name = 'index'),
    url(r'^nuevo$',login_required(PagoCreate.as_view()), name = 'pago_crear'),
    url(r'^listar',login_required(PagoList.as_view()), name = 'pago_listar'),
    url(r'^editar/(?P<pk>\d+)$',login_required(PagoUpdate.as_view()), name = 'pago_editar'),
    url(r'^eliminar/(?P<pk>\d+)$',login_required( PagoDelete.as_view()), name = 'pago_eliminar'),
    #url(r'^$', 'hola'),

]