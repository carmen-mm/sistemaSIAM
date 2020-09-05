from django.urls import path
from django.contrib.auth.decorators import login_required
# en la variable urlpatterns se listan todas las urls de LA VISTA de la apps beneficiario

from apps.beneficiario.views import BeneficiarioList, BeneficiarioInsert, BeneficiarioModificar, BeneficiarioEliminar, Opciones, ReportePDF #,hello_pdf

app_name = "beneficiario"

urlpatterns = [
   path('opciones/', login_required(Opciones), name='opciones'),
   path('listar/', login_required(BeneficiarioList.as_view()), name='listar'),
   path('insertar/', login_required(BeneficiarioInsert.as_view()), name='insertar'),
   path('modificar/<int:pk>',login_required( BeneficiarioModificar.as_view()), name='modificar'),
   path('eliminar/<int:pk>', login_required(BeneficiarioEliminar.as_view()), name='eliminar'),
   path('reporte/', login_required(ReportePDF.as_view()), name='reporte')
]