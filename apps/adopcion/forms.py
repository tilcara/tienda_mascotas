# -*- encoding:utf-8 -*-
from django import forms

from apps.adopcion.models import Persona, Solicitud



class PersonaForm(forms.ModelForm):

	class Meta:
		
		model = Persona
		
		fields = [
			'nombre',
			'apellido',
			'edad',
			'telefono',
			'email',
			'domicilio',
		]
		
		labels = {
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'edad': 'Edad',
			'telefono': 'Teléfono',
			'email': 'Correo electrónico',
			'domicilio': 'Domicilio',
		}
		
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellido':forms.TextInput(attrs={'class':'form-control'}),
			'edad':forms.NumberInput(attrs={'class':'form-control'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'domicilio':forms.TextInput(attrs={'class':'form-control'}),
		}


class SolicitudForm(forms.ModelForm):

	class Meta:
		
		model = Solicitud
		
		fields = [
			'numero_mascotas',
			'razones',	
		]
		
		labels = {
			'numero_mascotas': 'Numero de mascotas',
			'razones': 'Razones para adoptar',
			
		}
		
		widgets = {
			'numero_mascotas':forms.NumberInput(attrs={'class':'form-control'}),
			'razones':forms.Textarea(attrs={'class':'form-control'}),
		}