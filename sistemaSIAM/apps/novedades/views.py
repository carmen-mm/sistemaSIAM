from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from apps.novedades.models import Novedades
from apps.novedades.forms import NovedadesForm
from django.urls import reverse_lazy

# Create your views here.
class NovedadesList(ListView):

    model = Novedades
    template_name = 'novedades/mostrar_novedades.html'
    paginate_by = 10

class NovedadesInsert(CreateView):
    model = Novedades
    #Indico qué formulario voy a utilizar apps->novedades->forms.py
    form_class = NovedadesForm
    #Indico qué template voy a utilizar templates
    template_name = 'novedades/subir_novedades.html'
    #Luego de insertar una nueva novedades nos redirigimos a :
    success_url = reverse_lazy('novedades:mostrarN')

class NovedadesModificar(UpdateView):
    model = Novedades
    #Indico qué formulario voy a utilizar apps->novedades->forms.py
    form_class = NovedadesForm
    #Indico qué template voy a utilizar templates
    template_name = 'novedades/subir_novedades.html'
    #Luego de insertar una nueva novedades nos redirigimos a :
    success_url = reverse_lazy('novedades:mostrarN')

class NovedadesEliminar(DeleteView):
    model = Novedades
    success_url = reverse_lazy('novedades:mostrarN')