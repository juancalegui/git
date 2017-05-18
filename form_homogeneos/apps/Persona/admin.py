from django.contrib import admin
from apps.Persona.models import Persona

class PersonaModelAdmin(admin.ModelAdmin):
	#list_display_links = ['cuil','nombre', 'legajo']
	search_fields = ['cuil','nombre', 'legajo']
	list_filter = ['cuil','nombre', 'legajo']
	class Meta:
		model = Persona

admin.site.register(Persona,PersonaModelAdmin)






