from django.urls import path

# en la variable urlpatterns se listan todas las urls de LA VISTA de la apps centromedico


from apps.centromedico.views import CentroMedicoNuevo, CentroMedicoList, Opciones

app_name = "centromedico"

urlpatterns = [
   path('opcionesCM/', Opciones, name='opcionesCM'),
   path('nuevo/', CentroMedicoNuevo.as_view(), name='nuevo'),
   path('listarCM/', CentroMedicoList.as_view(), name='listarCM'),
]