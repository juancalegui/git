from django.conf.urls import url
from apps.SolicitudTramite.views import index

urlpatterns = [
    url(r'^nuevo$', index),]