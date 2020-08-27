from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from apps.beneficiario.models import Beneficiario
from apps.beneficiario.forms import BeneficiarioForm

class BeneficiarioList(ListView):

    model = Beneficiario
    template_name = 'beneficiario/listar_beneficiario.html'
    paginate_by = 10


class BeneficiarioInsert(CreateView):
    model = Beneficiario
    #Indico qué formulario voy a utilizar apps->beneficiario->forms.py
    form_class = BeneficiarioForm
    #Indico qué template voy a utilizar templates->beneficiario->insertar_beneficiario.html
    template_name = 'beneficiario/insertar_beneficiario.html'
    #Redirigimos luego de insertar un beneficiario nuevo
    success_url = reverse_lazy('beneficiario:listar')

class BeneficiarioModificar(UpdateView):
    model = Beneficiario
    # Indico qué formulario voy a utilizar apps->beneficiario->forms.py
    form_class = BeneficiarioForm
    # Indico qué template voy a utilizar templates->beneficiario->insertar_beneficiario.html
    template_name = 'beneficiario/insertar_beneficiario.html'
    # Redirigimos luego de insertar un beneficiario nuevo
    success_url = reverse_lazy('beneficiario:listar')

