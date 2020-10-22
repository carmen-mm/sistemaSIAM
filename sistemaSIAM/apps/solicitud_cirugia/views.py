from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.solicitud_cirugia.models import Cirugia, Solicitud_Cirugia
from apps.centromedico.models import CentroMedico
from apps.solicitud_cirugia.forms import CirugiaForm
from django.http import HttpResponse

# Create your views here.

class CirugiaLista(ListView):

    model = Solicitud_Cirugia
    template_name = 'cirugia/listarC.html'

class CirugiaNueva(CreateView):
    model = Solicitud_Cirugia
    form_class = CirugiaForm
    template_name = 'cirugia/registrar_cirugia.html'
    success_url = reverse_lazy('cirugia:listarC')

def Opciones(request):
  return render(request,'cirugia/opciones.html')