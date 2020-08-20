from django.urls import path

from apps.pedido_ambulatorio.views import index

# en la variable urlpatterns se listan todas las urls de las vistas de la aplicación beneficiario


urlpatterns = [
    path(r'^$', index), #el segundo parámetro que recibe path(,) es la vista de mi apps pedido_ambulatorio
]