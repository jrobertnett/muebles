#encoding:utf-8
from django import forms
from apps.clientes.models import Cliente

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente

	dpi = forms.CharField(widget=forms.NumberInput(attrs={
		'placeholder': 'DPI',
		'size': '13'}))
	nombre = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Nombre Cliente',
		'size': '40'}))
	apellidos = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Apellidos',
		'size': '40'}))
	direccion = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Direccion',
		'size': '40'}))
	telefono = forms.CharField(widget=forms.NumberInput(attrs={
		'placeholder': 'Telefono',
		'size': '8'}))

	def clean_dpi(self):
		diccionario_limpio = self.cleaned_data
		dpi = diccionario_limpio.get('dpi')
		if len(dpi) < 13 or len(dpi) > 13:
			raise forms.ValidationError("debe ser de 13 Digitos")
		return dpi

	def clean_nombre(self):
		nombre = self.cleaned_data['nombre']
		if not nombre.isalpha():
			raise forms.ValidationError('No puede contener números')
		return nombre
