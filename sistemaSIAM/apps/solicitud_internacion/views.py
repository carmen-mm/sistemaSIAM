from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.solicitud_internacion.models import Internacion
from apps.solicitud_internacion.forms import InternacionForm

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