
from django import forms
from apps.mascota.models import Mascota
                                      

class MascotaForm(forms.ModelForm):

	class Meta:
		
		model = Mascota

		fields = [
			'persona',
			'vacuna',
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rescate',
		]

		labels = {

			'persona':'Adoptante',
			'vacuna':'Vacuna',
			'nombre':'Nombre',
			'sexo':'Sexo',
			'edad_aproximada':'Edad Aproximada',
			'fecha_rescate':'Fecha Rescate',	
		}

		widgets = {

			'persona':forms.Select(attrs={'class':'form-control'}),
			'vacuna':forms.CheckboxSelectMultiple(),
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'sexo':forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_rescate':forms.DateInput(attrs={'class':'form-control'}),

		}