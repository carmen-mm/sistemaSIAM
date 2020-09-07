from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.novedades.views import NovedadesList, NovedadesInsert, NovedadesEliminar, NovedadesModificar

app_name = "novedades"

urlpatterns = [
   path('mostrarN/', NovedadesList.as_view(), name='mostrarN'),
   path('subir/', NovedadesInsert.as_view(), name='subir'),
   path('eliminarN/<int:pk>', NovedadesEliminar.as_view(), name='eliminarN'),
   path('modificarN/<int:pk>', NovedadesModificar.as_view(), name='modificarN'),
]