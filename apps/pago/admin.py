from django.contrib import admin
from apps.pago.models import Pago,Cliente

class PagoModelAdmin(admin.ModelAdmin):
	list_display = ['cliente', 'fecha_pago','fecha_vencimiento','cantidad']
	list_display_links = ['cliente', 'fecha_pago','fecha_vencimiento','cantidad']
	search_fields = ['fecha_pago']
	list_filter = ['cliente_id','fecha_pago']
	
	class Meta:
		model = Pago

admin.site.register(Pago, PagoModelAdmin)