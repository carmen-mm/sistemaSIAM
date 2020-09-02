from django.urls import path
# en la variable urlpatterns se listan todas las urls de LA VISTA de la apps usuario
from apps.usuario.views import RegistroUsuario
app_name = "usuario"

urlpatterns = [
   path('registrar/', RegistroUsuario.as_view(), name='registrar'),

]
