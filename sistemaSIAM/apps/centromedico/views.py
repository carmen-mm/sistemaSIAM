#Importamos settings para poder tener a la mano la ruta de la carpeta media
from django.conf import settings
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from apps.centromedico.models import CentroMedico
from apps.centromedico.forms import CentroMedicoForm

# Create your views here.

def Opciones(request):
  return render(request,'centromedico/opciones.html')


class CentroMedicoNuevo(CreateView):
    model = CentroMedico
    #Indico qué formulario voy a utilizar apps->beneficiario->forms.py
    form_class = CentroMedicoForm
    #Indico qué template voy a utilizar templates->beneficiario->insertar_beneficiario.html
    template_name = 'centromedico/nuevo.html'
    #Redirigimos luego de insertar un beneficiario nuevo
    success_url = reverse_lazy('centromedico:listarCM')

class CentroMedicoList(ListView):
    model = CentroMedico
    template_name = 'centromedico/listar.html'
    paginate_by = 15
    queryset = CentroMedico.objects.order_by('razonSocial')

class CentroMedicoModificar(UpdateView):
    model = CentroMedico
    # Indico qué formulario voy a utilizar apps->centromedico->forms.py
    form_class = CentroMedicoForm
    # Indico qué template voy a utilizar templates->centromedico->nuevo.html
    template_name = 'centromedico/nuevo.html'
    # Redirigimos luego de modificar un centromedico nuevo
    success_url = reverse_lazy('centromedico:listarCM')

class ReportePDF(View):
    pdf = canvas.Canvas("listado_CentroMedico.pdf")
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
        pdf.drawString(200, 700, u"LISTADO DE CENTROS MEDICOS")

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
        encabezados = ('RAZON SOCIAL', 'LOCALIDAD', 'DOMICILIO', 'TELEFONO')
        # Creamos una lista de tuplas que van a contener a lOS CENTROS MEDICOS
        detalles = [(centromedico.razonSocial, centromedico.localidad, centromedico.domicilio, centromedico.telefono) for centromedico in CentroMedico.objects.all()]
        # Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[7 * cm, 3 * cm, 3 * cm, 3 * cm])
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
