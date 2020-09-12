from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from apps.pedido_ambulatorio.models import Pedido_Ambulatorio, Detalle_PedidoMedico

class PedidoAmbulatorioForm(forms.ModelForm):
    class Meta:
        model = Pedido_Ambulatorio
        fields = (
            'idPedido',
            'fecha_ingreso',
            'beneficiario',
         )
        labels = {
            'idPedido': 'Pedido N°',
            'fecha_ingreso': 'Fecha Ingreso',
            'beneficiario': 'DNI Beneficiario',

        }

        widgets = {
            'idPedido': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control'}),
            'beneficiario': forms.Select(attrs={'class': 'form-control'}),
        }

class DetallesForm(forms.ModelForm):
    class Meta:
        model = Detalle_PedidoMedico
        fields = (
                'autorizado',
                'importeCoseguro',
                'observaciones',
                'pedido',
                'doctores',
                'practicas',
        )
