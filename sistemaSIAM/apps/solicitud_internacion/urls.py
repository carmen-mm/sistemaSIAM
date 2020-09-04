from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.solicitud_internacion.views import InternacionNueva, InternacionList, InternacionModificar, Opciones

app_name = "internacion"

urlpatterns = [
   path('opcionesI/', login_required(Opciones), name='opcionesI'),
   path('nuevaI/', login_required(InternacionNueva.as_view()), name='nuevaI'),
   path('listarI/', login_required(InternacionList.as_view()), name='listarI'),
   path('modificar/<int:pk>', login_required(InternacionModificar.as_view()), name='modificar'),
]