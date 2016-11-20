from django.contrib import admin
from apps.cliente.models import Cliente


# Register your models here.
class ClienteModelAdmin(admin.ModelAdmin):
	list_display = ['dni','nombre', 'apellido','domicilio']
	list_display_links = ['dni','nombre', 'apellido','domicilio']
	search_fields = ['nombre','apellido']
	list_filter = ['nombre','apellido']
	class Meta:
		model = Cliente

admin.site.register(Cliente, ClienteModelAdmin)