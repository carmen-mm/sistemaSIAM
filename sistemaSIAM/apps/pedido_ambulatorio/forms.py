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

class DetallesForm(forms.ModelForm):
    class Meta:
        model = Detalle_PedidoMedico
        fields = (
                'fecha_prescripcion',
                'autorizado',
                'importeCoseguro',
                'pedido',
                'doctores',
                'diagnosticos',
                'practicas',
        )
