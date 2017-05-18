from django  import forms
from apps.SolicitudTramite.models import SolicitudTramite 

class SolicitudTramiteForm(forms.ModelForm):

	class Meta:
		model = SolicitudTramite

		fields = [
            'id_solicitud',
            'fecha_creacion',
            'perso_cuil',
            'tramite',
            'tipo_tramite',
            'fecha_solicitada',
            'cant_dias',
            'motivo',
            'documentacion',

        ]
		labels = {
			
			'id_solicitud':'Nro de Solicitud',
            'fecha_creacion':'Fecha de creación',
            'perso_cuil':'Persona',
            'tramite':'Tramite',
            'tipo_tramite': 'Tipo Tramite',
            'fecha_solicitada': 'Fecha',
            'cant_dias':'Cantidad ',
            'motivo':'Motivo',
            'documentacion': 'Documentación',

        }
		widgest = {
			'id_solicitud': forms.TextInput(attrs = {'class': 'form-control'}),
			'fecha_creacion': forms.TextInput(attrs = {'class': 'form-control'}),
            'perso_cuil': forms.Select(attrs = {'class': 'form-control'}),
            'tramite': forms.Select(attrs = {'class': 'form-control'}),
            'tipo_tramite':forms.Select(attrs = { 'class':'form-control'}),
            'fecha_solicitada': forms.TextInput(attrs = {'class': 'form-control'}),
            'cant_dias': forms.TextInput(attrs = {'class': 'form-control'}),
            'motivo': forms.TextInput(attrs = {'class': 'form-control'}),
            'documentacion': forms.TextInput(attrs = {'class': 'form-control'}),

        }
       

