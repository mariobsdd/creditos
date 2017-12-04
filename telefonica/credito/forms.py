from django import forms
from models import Cliente


class ClienteForm(forms.ModelForm):

	# model related to the form
	class Meta:
		model = Cliente
		fields = ('cedula','salario','tel1','tel2','tel3','buro','telefonica')
		# cedula = forms.CharField(label="Ingrese num cedula",required = True)
		# salario = forms.FloatField()