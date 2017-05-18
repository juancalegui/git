from django.contrib import admin
from apps.TipoTramite.models import TipoTramite

class TipoTramiteModelAdmin(admin.ModelAdmin):
	#list_display_links = ['cuil','nombre', 'legajo']
	#search_fields = ['tramite']
	list_filter = ['tramite']
	class Meta:
		model = TipoTramite
admin.site.register(TipoTramite, TipoTramiteModelAdmin)

# Register your models here.
