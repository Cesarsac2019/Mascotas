# -*- encoding:utf-8 -*-
from django import forms

from apps.adopciones.models import Persona, Solicitud



class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona
		fields = [
			'nombre',
			'apellido',
            'fecha_nac',
			'edad',
			'telefono',
			'email',
			'domicilio',
		]
		labels = {
			'nombre': 'Nombre',
			'apellido': 'Apellidos',
            'fecha_nac':'Fecha de  Nacimiento',
            'edad': 'Edad',
			'telefono': 'Teléfono',
			'email': 'Correo electrónico',
			'domicilio': 'Domicilio',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nac':forms.DateInput(attrs={'class':'form-control'}),
			'edad':forms.TextInput(attrs={'class':'form-control'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'domicilio':forms.Textarea(attrs={'class':'form-control'}),
		}


class SolicitudForm(forms.ModelForm):

	class Meta:
		model = Solicitud
		fields = [
			'numero_ninios',
			'razones',
		]
		labels = {
			'numero_ninios': 'Numero de ninios',
			'razones': 'Razones para apadrinar',

		}
		widgets = {
			'numero_ninios':forms.TextInput(attrs={'class':'form-control'}),
			'razones':forms.Textarea(attrs={'class':'form-control'}),
		}
