from django.urls import path

# en la variable urlpatterns se listan todas las urls de LA VISTA de la apps centromedico


from apps.centromedico.views import CentroMedicoNuevo

app_name = "centromedico"

urlpatterns = [
   path('nuevo/', CentroMedicoNuevo.as_view(), name='nuevo'),

]