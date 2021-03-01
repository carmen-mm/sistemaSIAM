from django import forms
from apps.solicitud_cirugia.models import Solicitud_Cirugia

class CirugiaForm(forms.ModelForm):
    class Meta:
        model = Solicitud_Cirugia
        fields = (
                 'fecha_ingreso',
                 'estado_clave',
                 'material',
                 'prequirurgicos',
                 'fecha_cirugia',
                 'tipo_cirugia',
                 'importe_coseguro',
                 'observaciones',
                 'beneficiario',
                 'doctor',
                 'cirugia',
                 'centromedico',
         )
        labels = {
                'fecha_ingreso': 'Fecha Recepción',
                'estado_clave': 'Estado Clave',
                'material': '¿Requiere material?',
                'prequirurgicos': '¿Tiene prequirúrgicos?',
                'fecha_cirugia': 'Fecha cirugía',
                'tipo_cirugia': 'Tipo cirugía',
                'importe_coseguro': 'Importe coseguro',
                'observaciones': 'Observaciones',
                'beneficiario': 'Beneficiario',
                'doctor': 'Doctor solicitante',
                'cirugia': 'Cirugía',
                'centromedico': 'Lugar de cirugía',

        }

        widgets = {
                'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control'}),
                'estado_clave': forms.Select(attrs={'class': 'form-control'}),
                'fecha_cirugia': forms.DateInput(attrs={'class': 'form-control'}),
                'tipo_cirugia': forms.Select(attrs={'class': 'form-control'}),
                'importe_coseguro': forms.NumberInput(attrs={'class': 'form-control'}),
                'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
                'beneficiario': forms.Select(attrs={'class': 'form-control'}),
                'doctor': forms.Select(attrs={'class': 'form-control'}),
                'cirugia': forms.Select(attrs={'class': 'form-control'}),
                'centromedico': forms.Select(attrs={'class': 'form-control'}),

            }
