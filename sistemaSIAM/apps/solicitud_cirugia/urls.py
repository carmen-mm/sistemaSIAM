from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.solicitud_cirugia.views import CirugiaNueva, CirugiaLista, Opciones, CirugiaModificar, CirugiaEliminar, ReportePDF

app_name = "cirugia"

urlpatterns = [
    path('opcionesC/', login_required(Opciones), name='opcionesC'),
    path('nuevaC/', login_required(CirugiaNueva.as_view()), name='nuevaC'),
    path('modificarC/<int:pk>', login_required(CirugiaModificar.as_view()), name='modificarC'),
    path('eliminar/<int:pk>', login_required(CirugiaEliminar.as_view()), name='eliminar'),
    path('listarC/', login_required(CirugiaLista.as_view()), name='listarC'),
    path('reporte/', login_required(ReportePDF.as_view()), name='reporte'),
]
