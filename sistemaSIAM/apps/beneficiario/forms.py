from django import forms
from apps.beneficiario.models import Beneficiario

class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiario
        #exclude = ()
        fields = (
        'tipoDNI',
        'dni',
        'nombre',
        'apellidos',
        'afiliado',
        'nroAfiliado',
        'localidad',
         )

        labels = {
                 'tipoDNI': 'Tipo DNI',
                 'dni': 'DNI',
                 'nombre': 'Nombre',
                 'apellidos': 'Apellidos',
                 'afiliado': 'Afiliado',
                 'nroAfiliado': 'Afil.N°',
                 'localidad': 'Localidad',
         }

        widgets = {
                    'tipoDNI': forms.Select(attrs={'class': 'form-control'}),
                    'dni': forms.NumberInput(attrs={'class': 'form-control'}),
                    'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                    'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
                    'afiliado': forms.CheckboxInput(attrs={'class': 'form-control'}),
                    'nroAfiliado': forms.NumberInput(attrs={'class': 'form-control'}),
                    'localidad': forms.Select(attrs={'class': 'form-control'}),
                   }
