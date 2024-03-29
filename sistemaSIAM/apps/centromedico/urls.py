from django.urls import path
from django.contrib.auth.decorators import login_required
# en la variable urlpatterns se listan todas las urls de LA VISTA de la apps centromedico


from apps.centromedico.views import CentroMedicoNuevo, CentroMedicoList, Opciones, CentroMedicoModificar, ReportePDF

app_name = "centromedico"

urlpatterns = [
   path('opcionesCM/', login_required(Opciones), name='opcionesCM'),
   path('nuevo/', login_required(CentroMedicoNuevo.as_view()), name='nuevo'),
   path('listarCM/', login_required(CentroMedicoList.as_view()), name='listarCM'),
   path('modificarCM/<int:pk>',login_required(CentroMedicoModificar.as_view()), name='modificarCM'),
   path('reporteCM/', login_required(ReportePDF.as_view()), name='reporteCM')
]