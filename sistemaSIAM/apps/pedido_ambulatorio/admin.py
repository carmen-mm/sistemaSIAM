from django.contrib import admin

from apps.pedido_ambulatorio.models import PA_tiene_Practicas, Diagnostico, Practica_Medica, Pedido_Ambulatorio

# Register your models here.
admin.site.register(PA_tiene_Practicas)
admin.site.register(Diagnostico)
admin.site.register(Practica_Medica)
admin.site.register(Pedido_Ambulatorio)