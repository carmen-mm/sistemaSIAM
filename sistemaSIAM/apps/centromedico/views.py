from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.centromedico.models import CentroMedico
from apps.centromedico.forms import CentroMedicoForm


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