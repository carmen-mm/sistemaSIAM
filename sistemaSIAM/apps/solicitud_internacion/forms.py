from django import forms
from apps.solicitud_internacion.models import Internacion

class InternacionForm(forms.ModelForm):
    class Meta:
        model = Internacion
        fields = (
            'fecha_ingreso',
            'fecha_egreso',
            'dias_dados',
            'dias_prorroga',
            'tipo1_internacion',
            'tipo2_internacion',
            'previa',
            'beneficiario',
            'doctorTratante',
            'centromedico',
            'diagnostico',
         )

        labels = {
            'fecha_ingreso': 'Fecha Ingreso',
            'fecha_egreso': 'Fecha Egreso',
            'dias_dados': 'Días autorizados',
            'dias_prorroga': 'Días de Prórroga',
            'tipo1_internacion': 'Internación',
            'tipo2_internacion': 'Tipo internación',
            'previa': 'Previa',
            'beneficiario' : 'Beneficiario',
            'doctorTratante': 'Doctor Tratante',
            'centromedico': 'Centro Médico',
            'diagnostico': 'Motivo de Internación',

         }

        widgets = {
                    'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control'}),
                    'fecha_egreso': forms.DateInput(attrs={'class': 'form-control'}),
                    'dias_dados': forms.NumberInput(attrs={'class': 'form-control'}),
                    'dias_prorroga': forms.NumberInput(attrs={'class': 'form-control'}),
                    'tipo1_internacion': forms.Select(attrs={'class': 'form-control'}),
                    'tipo2_internacion': forms.Select(attrs={'class': 'form-control'}),
                    'previa': forms.Select(attrs={'class': 'form-control'}),
                    'beneficiario': forms.Select(attrs={'class': 'form-control'}),
                    'doctorTratante': forms.Select(attrs={'class': 'form-control'}),
                    'centromedico': forms.Select(attrs={'class': 'form-control'}),
                    'diagnostico': forms.Select(attrs={'class': 'form-control'}),
         }
