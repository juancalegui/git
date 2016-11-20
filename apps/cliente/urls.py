from django.conf.urls import url
from apps.cliente.views import index,ClienteList, ClienteCreate, ClienteUpdate, ClienteDelete
from django.contrib.auth.decorators import login_required
urlpatterns = [
    #url(r'^$', index),
    #url(r'^$', index, name = 'index'),
    url(r'^nuevo$',login_required( ClienteCreate.as_view()), name = 'cliente_crear'),
    url(r'^listar',login_required( ClienteList.as_view()), name = 'cliente_listar'),
    url(r'^editar/(?P<pk>\d+)$',login_required(ClienteUpdate.as_view()), name = 'cliente_editar'),
    url(r'^eliminar/(?P<pk>\d+)$',login_required(ClienteDelete.as_view()), name = 'cliente_eliminar'),
   # url('clientelistable/$', ClienteListable.as_view(), name="clientelistable"),

]