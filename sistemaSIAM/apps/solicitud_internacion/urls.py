from django.urls import path


from apps.solicitud_internacion.views import InternacionNueva, InternacionList, InternacionModificar, Opciones

app_name = "internacion"

urlpatterns = [
   path('opcionesI/', Opciones, name='opcionesI'),
   path('nuevaI/', InternacionNueva.as_view(), name='nuevaI'),
   path('listarI/', InternacionList.as_view(), name='listarI'),
   path('modificar/<int:pk>', InternacionModificar.as_view(), name='modificar'),
]