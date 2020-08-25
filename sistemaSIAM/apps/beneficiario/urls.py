from django.urls import path
# en la variable urlpatterns se listan todas las urls de las vistas de la aplicación beneficiario

'''
urlpatterns = [
    path(r'^$', index), #el segundo parámetro que recibe path(,) es la vista de mi apps beneficiario
]
'''


from apps.beneficiario.views import BeneficiarioList, BeneficiarioInsert

urlpatterns = [
    path('listar/', BeneficiarioList.as_view(), name='listar'),
    path('insertar/', BeneficiarioInsert.as_view(), name='insertar'),
]
