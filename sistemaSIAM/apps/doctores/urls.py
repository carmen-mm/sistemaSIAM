from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.doctores.views import EspecialidadList, DoctoresList, DoctorNuevo, ReporteDoctores

# en urlpatterns se listan todas las urls de las vistas de la app doctores
app_name = "doctores"

urlpatterns = [
   path('listarE/', login_required(EspecialidadList.as_view()), name='listarE'), #el tercer parámetro es el nombre de la URL para identificar a la vista
   path('listarDoc/', login_required(DoctoresList.as_view()), name='listarDoc'),
   path('nuevoDoc/', login_required(DoctorNuevo.as_view()), name='nuevoDoc'),
   path('reporteDoc/', ReporteDoctores.as_view(), name='reporteDoc'),
]