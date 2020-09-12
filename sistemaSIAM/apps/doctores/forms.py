from django.forms import ModelForm
from django import forms
from apps.doctores.models import Doctor
from django.core.mail import EmailMessage

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = (
            'matriculaMP',
            'matriculaME',
            'cuit',
            'nombre',
            'apellidos',
            'especialidad',
            'convenioOSECAC',
         )

        labels = {
            'matriculaMP': 'Matrícula Provincial',
            'matriculaME': 'Matrícula Especialidad',
            'cuit': 'CUIT',
            'nombre': 'Nombre',
            'apellidos': 'Apellido',
            'especialidad': 'Especialidades',
            'convenioOSECAC': '¿Tiene convenio con OSECAC?',

         }

        widgets = {
                  'matriculaMP': forms.NumberInput(attrs={'class': 'form-control'}),
                  'matriculaME': forms.NumberInput(attrs={'class': 'form-control'}),
                  'cuit': forms.TextInput(attrs={'class': 'form-control'}),
                  'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                  'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
                  'trabaja_en': forms.Select(attrs={'class': 'form-control'}),
                  'especialidad': forms.CheckboxSelectMultiple(),
                  'convenioOSECAC': forms.Select(attrs={'class': 'form-control'}),

            }
