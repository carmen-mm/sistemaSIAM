from django import forms
from apps.novedades.models import Novedades

class NovedadesForm(forms.ModelForm):
    class Meta:
        model = Novedades
        fields = [
                    'fecha',
                    'titulo',
                    'mensaje',

            ]

        labels = {
                 'fecha':'Fecha',
                 'titulo':'Título',
                 'mensaje':'Mensaje',

         }

        widgets = {
                    'fecha': forms.DateInput(attrs={'class': 'form-control'}),
                    'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                    'mensaje': forms.TextInput(attrs={'class': 'form-control'}),

                   }
