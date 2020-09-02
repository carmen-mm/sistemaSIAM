from django.urls import path

from apps.pedido_ambulatorio.views import index, DiagnosticoList

# en urlpatterns se listan todas las urls de las vistas de la app pedido_ambulatorio
app_name = "practicasMedicas"

urlpatterns = [
    path('', index, name='index'), #el segundo parámetro que recibe path(,) es la vista de mi apps pedido_ambulatorio
    path('listarD', DiagnosticoList.as_view()), #el tercer parámetro es el nombre de la URL para identificar a la vista
]

