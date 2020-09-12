from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.solicitud_cirugia.views import CirugiaNueva, CirugiaLista

app_name = "cirugias"

urlpatterns = [
    path('nuevaC/', login_required(CirugiaNueva.as_view()), name='nuevaC'),
    path('listarC/', login_required(CirugiaLista.as_view()), name='listarC'),
]
