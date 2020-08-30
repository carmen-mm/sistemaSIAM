from django import forms
from apps.doctores.models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = (
            'matriculaDoc',
            'cuit',
            'nombre',
            'apellido',
            'especialidades',
            'telefono',
            'domicilio',
            'email',
            'convenioOSECAC',
         )

        labels = {
            'matriculaDoc':'Matrícula',
            'cuit': 'CUIT',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'especialidades': 'Especialidades',
            'telefono' : 'Teléfono',
            'domicilio': 'domicilio',
            'email': 'E-mail',
            'convenioOSECAC': '¿Tiene convenio con OSECAC?',

         }

        widgets = {
                  'matriculaDoc': forms.IntegerField(attrs={'class': 'form-control'}),
                  'cuit': forms.TextInput(attrs={'class': 'form-control'}),
                  'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                  'apellido': forms.TextInput(attrs={'class': 'form-control'}),
                  'especialidades': forms.CheckboxSelectMultiple(),
                  'telefono': forms.TextInput(attrs={'class': 'form-control'}),
                  'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
                  'email': forms.EmailField(attrs={'class': 'form-control'}),
                  'convenioOSECAC': forms.Select(attrs={'class': 'form-control'}),

            }
