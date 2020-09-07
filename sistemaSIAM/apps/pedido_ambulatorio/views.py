from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import formset_factory, modelformset_factory
from django.forms import inlineformset_factory
from django.views.generic.edit import FormView
from django.forms import inlineformset_factory
from apps.pedido_ambulatorio.forms import PedidoAmbulatorioForm, DetallesForm
from django.views.generic import ListView
from django.urls import reverse_lazy
from apps.pedido_ambulatorio.models import Diagnostico, Detalle_PedidoMedico, Pedido_Ambulatorio



def index(request):
  return render(request,'practicasMedicas/index.html')


class DiagnosticoList(ListView):
    model = Diagnostico
    template_name = 'practicasMedicas/diagnostico.html'
    paginate_by = 15



def Detalle_Pedido(request):
    ItemFormSet = inlineformset_factory(
        Pedido_Ambulatorio,
        Detalle_PedidoMedico,
        form=DetallesForm,
        fields=('fecha_prescripcion',
                'autorizado',
                'importeCoseguro',
                'pedido',
                'doctores',
                'diagnosticos',
                'practicas',),
        extra=4
    )
    form = PedidoAmbulatorioForm()
    formset = ItemFormSet()
    if request.method == 'POST':
        form = PedidoAmbulatorioForm(request.POST)
        formset = ItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            url = reverse_lazy('centromedico:listarCM')
            return HttpResponseRedirect(url)
    return render(request, 'practicasMedicas/detallePedido.html', {
        'form': form,
        'formset': formset
    })