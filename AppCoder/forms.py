from django import forms

class PagoFormulario(forms.Form):
    tipo_tarjeta=forms.CharField(max_length=40)
    cuotas=forms.IntegerField()

class ProductosFormulario(forms.Form):
    categoria = forms.CharField()
    rango_precio=forms.IntegerField()
   
class VendedoresFormulario(forms.Form):
    localidad=forms.CharField()
    tiempo_de_entrega=forms.IntegerField()
    calificacion=forms.IntegerField()