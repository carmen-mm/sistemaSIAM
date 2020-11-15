from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from apps.pedido_ambulatorio.forms import PedidoAmbulatorioForm, DetallesForm
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from apps.pedido_ambulatorio.models import Diagnostico, Detalle_PedidoMedico, Pedido_Ambulatorio
from datetime import datetime
from django.db.models import Max
import simplejson


def Opciones(request):
  return render(request, 'practicasMedicas/opciones.html')

def index(request):
  return render(request, 'practicasMedicas/index.html')


class DiagnosticoList(ListView):
    model = Diagnostico
    template_name = 'practicasMedicas/diagnostico.html'
    paginate_by = 15


def Detalle_Pedido(request):
    ItemFormSet = inlineformset_factory(
        Pedido_Ambulatorio,
        Detalle_PedidoMedico,
        form=DetallesForm,
        extra=3
    )
    form = PedidoAmbulatorioForm(request.POST or None)
    formset = ItemFormSet(request.POST or None, instance=form.instance)
    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            paf = form.save(commit=False)
            paf.user = request.user
            paf.save()
            formset.save()
            url = reverse_lazy('practicasMedicas:listarP')
            return HttpResponseRedirect(url)
    return render(request, 'practicasMedicas/detallePedido.html', {'form': form, 'formset': formset })

class PedidosListar(ListView):
    model = Pedido_Ambulatorio
    template_name = 'practicasMedicas/listar_pedidos.html'
    paginate_by = 15

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        if filter_val=='':
            new_context = Pedido_Ambulatorio.objects.all()
        else:
            new_context = Pedido_Ambulatorio.objects.filter(
                idPedido=filter_val,
            )
        return new_context


    def get_context_data(self, **kwargs):
        context = super(PedidosListar, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        return context

class PedidoModificar(UpdateView):
    model = Pedido_Ambulatorio
    form_class = PedidoAmbulatorioForm
    template_name = 'practicasMedicas/detallePedido.html'

    def get_success_url(self):
        self.success_url = reverse_lazy('practicasMedicas:listarP')
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super(PedidoModificar, self).get_context_data(**kwargs)
        ItemFormSet = inlineformset_factory(
            Pedido_Ambulatorio,
            Detalle_PedidoMedico,
            form=DetallesForm,
            extra=3
        )
        if self.request.POST:
            context['formset'] = ItemFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = ItemFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

def ObtenerUltimoIdPedido(request):
    fecha = request.GET.get('fecha')
    result = {}
    result['data'] = []

    try:
        numero = 1

        print(fecha)

        list_query = {}
        list_query['pedido__fecha_ingreso'] = datetime.strptime(fecha, '%d/%m/%Y').strftime('%Y-%m-%d')

        max_num = Detalle_PedidoMedico.objects.filter(**list_query).aggregate(Max('pedido__idPedido'))
        if max_num and max_num['pedido__idPedido__max']:
            numero = int(max_num['pedido__idPedido__max']) + 1

        result['numero'] = numero
    except Exception:
        result['numero'] = ""
    return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type='application/json')