from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.doctores.models import Especialidad, Doctor
from apps.doctores.forms import DoctorForm

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