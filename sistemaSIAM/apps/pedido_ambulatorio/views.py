from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from apps.pedido_ambulatorio.forms import PedidoAmbulatorioForm, DetallesForm
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.pedido_ambulatorio.models import Diagnostico, Detalle_PedidoMedico, Pedido_Ambulatorio
from datetime import datetime
from django.db.models import Max
import simplejson

from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


class ReportePDF(View):
    pdf = canvas.Canvas("listado_PedidosAmbulatorios.pdf")
    pdf.save()
    def cabecera(self, pdf):
        # Utilizamos el archivo siam.png que está guardado en la carpeta media
        archivo_imagen = settings.MEDIA_ROOT + '/siam.png'
        # Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 30, 680, 200, 200, preserveAspectRatio=True)           #40, 750, 120, 90,
        # Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 30)
        # Dibujamos una cadena en la ubicación X,Y especificada
        #pdf.drawString(230, 600, u"SIAM ")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 700, u"LISTADO DE PEDIDOS AMBULATORIOS")

    def get(self, request, *args, **kwargs):
        # Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        # La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        # Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        # Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf, y)
        # Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self, pdf, y):
        # Creamos una tupla de encabezados para nuestra tabla
        encabezados = ('FECHA', 'PEDIDO N°', 'BENEFICIARIO')
        # Creamos una lista de tuplas que van a contener a los pedidos
        detalles = [(p.fecha_ingreso, p.idPedido, p.beneficiario) for p in Pedido_Ambulatorio.objects.all()]
        # Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[3 * cm, 5 * cm, 10 * cm])
        # Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                # La primera fila(encabezados) va a estar centrada
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                # Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                # El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        # Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        # Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60, y)




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
    return render(request, 'practicasMedicas/detallePedido.html', {'form': form, 'formset': formset})

class PedidosListar(ListView):
    model = Pedido_Ambulatorio
    template_name = 'practicasMedicas/listar_pedidos.html'
    paginate_by = 15

    # def get_queryset(self):
    #    filter_val = self.request.GET.get('filter', '')
    #   if filter_val=='':
    #       new_context = Pedido_Ambulatorio.objects.all()
    #   else:
    #       new_context = Pedido_Ambulatorio.objects.filter(
    #           idPedido=filter_val,
    #       )
    #   return new_context
    def get_queryset(self):
        filter_pedido_val = self.request.GET.get('filter_pedido', '')
        filter_fecha_val = self.request.GET.get('filter_fecha', '')
        filter_apellido_val = self.request.GET.get('filter_apellido', '')
        if len(filter_pedido_val) > 0:
            new_context = Pedido_Ambulatorio.objects.filter(idPedido=filter_pedido_val)
        elif len(filter_fecha_val) > 0:
            new_context = Pedido_Ambulatorio.objects.filter(fecha_ingreso=datetime.strptime(filter_fecha_val, '%d/%m/%Y').strftime('%Y-%m-%d'))
        elif len(filter_apellido_val) > 0:
            new_context = Pedido_Ambulatorio.objects.filter(beneficiario__apellidos__icontains=filter_apellido_val)
        else:
            new_context = Pedido_Ambulatorio.objects.all()
        return new_context


    # def get_queryset(self):
    #     filter_val = self.request.GET.get('filter', '')
    #     if filter_val=='':
    #        new_context = Pedido_Ambulatorio.objects.all()
    #     else:
    #        new_context = Pedido_Ambulatorio.objects.filter(beneficiario_id=filter_val,)
    #     return new_context



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
        list_query = {}
        list_query['pedido__fecha_ingreso'] = datetime.strptime(fecha, '%d/%m/%Y').strftime('%Y-%m-%d')

        max_num = Detalle_PedidoMedico.objects.filter(**list_query).aggregate(Max('pedido__idPedido'))
        if max_num and max_num['pedido__idPedido__max']:
            numero = int(max_num['pedido__idPedido__max']) + 1

        result['numero'] = numero
    except Exception:
        result['numero'] = ""
    return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type='application/json')