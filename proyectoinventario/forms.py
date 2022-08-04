from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from proyectoinventario.models import Assets, Clientes
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
    fecha_compra = forms.DateTimeField(
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
        choices=(('stock', "Stock"), ('dañado', "Dañado")),

    )
    estado = forms.TypedChoiceField(
        choices=(('nuevo', "Nuevo"), ('garantia', "Garantia"),
                 ('funcional', "Funcional"), ('baja', "Baja")),
        required=True,

    )
    accion = forms.TypedChoiceField(
        required=True,
        choices=((1, "Entrada"), (0, "Salida")),
        initial='1',
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Assets
        fields = ['modelo', 'serie', 'marca', 'cantidad',
                  'fecha_compra', 'tipo', 'categoria', 'estado', 'accion']
        wigets = {'fecha': forms.DateTimeInput(
            format='%d/%m/%Y', attrs={'type': 'datetime'})}


class FormSalidas(forms.ModelForm):
    nombre = forms.CharField(
        required=True
    )
    email = forms.EmailField(
        required=True
    )
    departamento = forms.CharField(
        required=True
    )
    hotel = forms.TypedChoiceField(
        choices=(('Comunes', "Comunes"), ('MYB', "Mar y Beach"),
                 ('LYM', "Lindo y Maya"), ('Grand', "Grand")),
        required=True
    )

    descripcion = forms.CharField(
        required=True
    )
    estado = forms.TypedChoiceField(
        choices=(('nuevo', "Nuevo"), ('garantia', "Garantia"),
                 ('funcional', "Funcional"), ('baja', "Baja")),
        required=True,
    )

    class Meta:
        model = Clientes
        fields = ['nombre', 'email', 'departamento',
                  'hotel', 'descripcion', 'estado']
        wigets = {'update': forms.DateTimeInput(
            format='%d/%m/%Y', attrs={'type': 'datetime'})}
