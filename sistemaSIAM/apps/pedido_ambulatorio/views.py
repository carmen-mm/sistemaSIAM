from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request,'practicasMedicas/index.html')


from django.views.generic import ListView

from apps.pedido_ambulatorio.models import Diagnostico

class DiagnosticoList(ListView):
    model = Diagnostico
    template_name = 'practicasMedicas/diagnostico.html'
    paginate_by = 15