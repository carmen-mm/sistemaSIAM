from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.usuario.forms import RegistroForm


# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrarUsuario.html'
    form_class = RegistroForm
    success_url = reverse_lazy('practicasMedicas:index')
