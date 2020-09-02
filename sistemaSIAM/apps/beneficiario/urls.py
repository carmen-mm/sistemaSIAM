from django.urls import path

# en la variable urlpatterns se listan todas las urls de LA VISTA de la apps beneficiario


from apps.beneficiario.views import BeneficiarioList, BeneficiarioInsert, BeneficiarioModificar, BeneficiarioEliminar, Opciones

app_name = "beneficiario"

urlpatterns = [
   path('opciones/', Opciones, name='opciones'),
   path('listar/', BeneficiarioList.as_view(), name='listar'),
   path('insertar/', BeneficiarioInsert.as_view(), name='insertar'),
   path('modificar/<int:pk>', BeneficiarioModificar.as_view(), name='modificar'),
   path('eliminar/<int:pk>', BeneficiarioEliminar.as_view(), name='eliminar')
]
