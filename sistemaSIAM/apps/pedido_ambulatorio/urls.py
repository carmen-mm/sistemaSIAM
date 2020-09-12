from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.pedido_ambulatorio.views import index, DiagnosticoList, Detalle_Pedido, PedidosListar, Opciones, PedidoModificar

# en urlpatterns se listan todas las urls de las vistas de la app pedido_ambulatorio
app_name = "practicasMedicas"

urlpatterns = [
    path('', login_required(index), name='index'), #el segundo parámetro que recibe path(,) es la vista de mi apps pedido_ambulatorio
    path('listarD', login_required(DiagnosticoList.as_view())), #el tercer parámetro es el nombre de la URL para identificar a la vista
    path('detalle', Detalle_Pedido, name='detalle'),
    path('listarP', PedidosListar.as_view(), name='listarP'),
    path('modificar/<int:pk>', PedidoModificar.as_view(), name='modificar'),
    path('opciones', Opciones, name='opciones')

]

