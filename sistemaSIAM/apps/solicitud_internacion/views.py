from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.solicitud_internacion.models import Internacion
from apps.centromedico.models import CentroMedico
from apps.solicitud_internacion.forms import InternacionForm
from django.http import HttpResponse

import simplejson
import datetime

# Create your views here.

def Opciones(request):
  return render(request,'internacion/opciones.html')

class InternacionList(ListView):

    model = Internacion
    template_name = 'internacion/listarI.html'


class InternacionNueva(CreateView):
    model = Internacion

    #Indico qué formulario voy a utilizar apps->solicitud_internacion->forms.py
    form_class = InternacionForm

    #Indico qué template voy a utilizar templates->internacion->nuevo.html
    template_name = 'internacion/nuevo.html'

    #Luego de cargar una nueva internación nos redirigimos al listado de internaciones
    success_url = reverse_lazy('internacion:listarI')

class InternacionModificar(UpdateView):
    model = Internacion
    # Indico qué formulario voy a utilizar apps->solicitud_internacion->forms.py
    form_class = InternacionForm
    # Indico qué template voy a utilizar templates->internacion->nuevo.html
    template_name = 'internacion/nuevo.html'
    # Redirigimos luego de insertar una internacion nueva
    success_url = reverse_lazy('internacion:listarI')

def DoctoresPorCentroMedico(request):
    id_centromedico = request.GET.get('id_centromedico')
    result = {}
    result['data'] = []
    if id_centromedico:
        doctores = []
        for doc in CentroMedico.objects.get(id=id_centromedico).doctores.values():
            doctores.append({
                'cuit': doc['cuit'],
                'nombre': doc['apellidos'] + " " + doc['nombre']
            })
        result['data'] = doctores
    return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type='application/json')

def CalcularProrroga(request):
    fecha_ingreso = request.GET.get('fecha_ingreso')
    fecha_egreso = request.GET.get('fecha_egreso')
    dias_dados = request.GET.get('dias_dados')
    result = {}
    result['data'] = []
    if fecha_ingreso and fecha_egreso and dias_dados:
        fecha_ingreso_date = datetime.datetime.strptime(fecha_ingreso, '%d/%m/%Y')
        fecha_egreso_date = datetime.datetime.strptime(fecha_egreso, '%d/%m/%Y')
        resta_fechas = fecha_egreso_date - fecha_ingreso_date
        calculo_dias = resta_fechas.days - int(dias_dados)
        if calculo_dias > 0:
            dias_prorroga = calculo_dias
        else:
            dias_prorroga = 0
        result['dias_prorroga'] = dias_prorroga
    return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type='application/json')