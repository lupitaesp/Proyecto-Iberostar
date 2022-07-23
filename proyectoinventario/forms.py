from django import forms

from proyectoinventario.models import Assets

class FormAssets(forms.ModelForm):
    class Meta:
        model= Assets
        fields = '__all__'
        wigets = {'fecha':forms.DateInput(attrs={'type':'date'})}


