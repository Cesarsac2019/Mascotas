from django import forms
from .models import Ninio


class NinioForm(forms.ModelForm):

	class Meta:
		model = Ninio

		fields = '__all__'
		labels = {
				'nombre': 'Nombre',
				'sexo': 'Sexo',
				'fecha_nac':'Fecha de nacimiento',
				'edad': 'Edad',
				'persona': 'Adoptante',
				'aportacion': 'Aportaciones',
		}
		widgets = {
				'nombre': forms.TextInput(attrs={'class':'form-control'}),
				'sexo': forms.TextInput(attrs={'class':'form-control'}),
				'fecha_nac': forms.TextInput(attrs={'class':'form-control'}),
				'edad': forms.TextInput(attrs={'class':'form-control'}),
				'persona': forms.Select(attrs={'class':'form-control'}),
				'aportacion': forms.CheckboxSelectMultiple(),
		}
