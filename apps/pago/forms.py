from django  import forms
from apps.pago.models import Pago 

class PagoForm(forms.ModelForm):

	class Meta:
		model = Pago

		fields = [
            'cliente',
            'fecha_pago',
            'fecha_vencimiento',
            'cantidad',
            

        ]
		labels = {
         	'clienta':'Cliente',
            'fecha_pago':'Fecha Pago',
            'fecha_vencimiento': 'Fecha Vencimiento ',
            'cantidad': 'Cantidad',
            
        }
        

		widgest = {
			'cliente': forms.Select(attrs = {'class': 'form-control'}),
            'fecha_pago': forms.TextInput(attrs = {'class': 'form-control'}),
            'fecha_vencimiento': forms.TextInput(attrs = {'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs = {'class': 'form-control'}),
        }

        
       
       