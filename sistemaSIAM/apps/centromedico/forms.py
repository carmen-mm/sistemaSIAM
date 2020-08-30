from django import forms
from apps.centromedico.models import CentroMedico

class CentroMedicoForm(forms.ModelForm):
    class Meta:
        model = CentroMedico
        fields = (
            'localidad',
            'razonSocial',
            'domicilio',
            'telefono',
            'e_mail',
            'especialidades',
            'doctores',
         )

        labels = {
            'localidad': 'Localidad',
            'razonSocial': 'Razón Social',
            'domicilio': 'Domicilio',
            'telefono': 'Teléfonos',
            'e_mail': 'E-mail',
            'especialidades': 'Especialidades',
            'doctores': 'Doctores',

         }

        widgets = {
                 'localidad': forms.Select(attrs={'class': 'form-control'}),
                  'razonSocial': forms.TextInput(attrs={'class': 'form-control'}),
                  'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
                  'telefono': forms.TextInput(attrs={'class': 'form-control'}),
                  'e_mail': forms.TextInput(attrs={'class': 'form-control'}),
                  'especialidades': forms.CheckboxSelectMultiple(),
                  'doctores': forms.CheckboxSelectMultiple(),

            }
