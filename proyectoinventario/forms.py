from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from proyectoinventario.models import Assets
from crispy_forms.helper import FormHelper

class FormAssets(forms.ModelForm):
    modelo = forms.CharField(
         required=True,
     )
    serie = forms.CharField(
         required=True,
     )
    marca = forms.CharField(
         required=True,
     )
    año_compra = forms.IntegerField(
        required=True,
        
    )
    cantidad = forms.IntegerField(
         required=True,
     )
    tipo = forms.CharField(
         required=True,
     )
    categoria = forms.TypedChoiceField(
         required=True,
         choices = (('stock', "Stock"), ('dañado', "Dañado")),
        
     )
    estado = forms.TypedChoiceField(
         choices = (('nuevo', "Nuevo"),('garantia', "Garantia"),('funcional', "Funcional"), ('baja', "Baja")),
         required=True,
      
     )
    accion = forms.TypedChoiceField(
         required=True,
         choices = ((1, "Entrada"), (0, "Salida")),
         initial = '1',
         widget = forms.RadioSelect,
     )
    
    
    class Meta:
        model= Assets
        fields = ['modelo','serie','marca','cantidad','año_compra','tipo','categoria','estado','accion']
        wigets = {'fecha':forms.DateTimeInput(format='%d/%m/%Y', attrs={'type': 'datetime'})}
 

