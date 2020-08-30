from django.urls import path

from apps.doctores.views import EspecialidadList, DoctoresList

# en urlpatterns se listan todas las urls de las vistas de la app doctores
app_name = "doctores"

urlpatterns = [
   path('listarE/', EspecialidadList.as_view(), name='listarE'), #el tercer parámetro es el nombre de la URL para identificar a la vista
   path('listarDoc/', DoctoresList.as_view(), name='listarDoc'),
]