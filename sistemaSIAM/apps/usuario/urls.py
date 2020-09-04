from django.urls import path
from django.contrib.auth.decorators import login_required
# en la variable urlpatterns se listan todas las urls de LA VISTA de la apps usuario
from apps.usuario.views import RegistroUsuario

app_name = "usuario"

urlpatterns = [
   path('registrar/', login_required(RegistroUsuario.as_view()), name='registrar'),
]
