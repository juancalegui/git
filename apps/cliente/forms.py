from django  import forms
from apps.cliente.models import Cliente 

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields = [
            'nombre',
            'apellido',
            'dni',
            'domicilio',

        ]
		labels = {
         	'nombre':'Nombre',
            'apellido':'Apellido',
            'dni':'DNI',
            'domicilio': 'Domicilio',
        }
		widgest = {
			'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'apellido': forms.TextInput(attrs = {'class': 'form-control'}),
            'dni': forms.TextInput(attrs = {'class': 'form-control'}),
            'domicilio':forms.TextInput(attrs = { 'class':'form-control'}),
        }
