from django.conf import settings
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView

from apps.doctores.models import Especialidad, Doctor
from apps.centromedico.models import CentroMedico
from apps.doctores.forms import DoctorForm

# Create your views here.
class EspecialidadList(ListView):
    model = Especialidad
    template_name = 'doctores/espe.html'
    paginate_by = 15

class DoctoresList(ListView):
    model = Doctor
    template_name = 'doctores/lista_doc.html'
    paginate_by = 15
    queryset = Doctor.objects.order_by('apellidos')
    context_object_name = "obj"

'''    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
'''

class DoctorNuevo(CreateView):
    model = Doctor

    #Indico qué formulario voy a utilizar apps->doctores->forms.py
    form_class = DoctorForm

    #Indico qué template voy a utilizar templates->doctores->nuevo.html
    template_name = 'doctores/nuevo.html'

    #Luego de crear un nuevo Doctor nos redirigimos a la lista de doctores
    success_url = reverse_lazy('doctores:listarDoc')

class DoctorModificar(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctores/nuevo.html'
    success_url = reverse_lazy('doctores:listarDoc')


class DoctorModificar(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctores/nuevo.html'
    success_url = reverse_lazy('doctores:listarDoc')

    def get_context_data(self, **kwargs):
        context = super(DoctorModificar, self).get_context_data(**kwargs)
        direcciones = "DIRECCIONES: "
        for cm in CentroMedico.objects.all():
            for doc in cm.doctores.values():
                if doc['cuit'] == context['doctor'].cuit:
                    direcciones += " | " + cm.razonSocial + " - " + cm.domicilio + " - " + cm.telefono
        context['direcciones'] = direcciones
        return context

class ReporteDoctores(View):
    pdf = canvas.Canvas("listado_doctores.pdf")
    pdf.save()
    def cabecera(self, pdf):
        # Utilizamos el archivo hola.png que está guardado en la carpeta media
        archivo_imagen = settings.MEDIA_ROOT + '/siam.png'
        # Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 30, 680, 200, 200, preserveAspectRatio=True)           #40, 750, 120, 90,
        # Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 30)
        # Dibujamos una cadena en la ubicación X,Y especificada
        #pdf.drawString(230, 600, u"SIAM ")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 710, u"LISTADO DE DOCTORES")

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
        encabezados = ('NOMBRE', 'DOMICILIO', 'TELEFONO', 'CONV')
        # Creamos una lista de tuplas que van a contener a las personas
        detalles = [(doctor.apellidos + doctor.nombre, doctor.convenioOSECAC) for doctor in Doctor.objects.all()]
        # Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[5 * cm, 5 * cm, 5 * cm, 2 * cm])
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
