from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView

from apps.doctores.models import Especialidad, Doctor

class EspecialidadList(ListView):
    model = Especialidad
    template_name = 'doctores/espe.html'
    paginate_by = 15

class DoctoresList(ListView):
    model = Doctor
    template_name = 'doctores/lista_doc.html'
    paginate_by = 15