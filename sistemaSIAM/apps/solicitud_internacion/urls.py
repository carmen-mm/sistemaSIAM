from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.solicitud_internacion.views import InternacionNueva, InternacionList, InternacionModificar, Opciones, DoctoresPorCentroMedico

app_name = "internacion"

urlpatterns = [
   path('opcionesI/', login_required(Opciones), name='opcionesI'),
   path('nuevaI/', login_required(InternacionNueva.as_view()), name='nuevaI'),
   path('listarI/', login_required(InternacionList.as_view()), name='listarI'),
   path('modificar/<int:pk>', login_required(InternacionModificar.as_view()), name='modificar'),
   path('doctor_por_centro_medico/', login_required(DoctoresPorCentroMedico), name='doctor_por_centro_medico'),
]