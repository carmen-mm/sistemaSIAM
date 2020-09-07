from django.contrib import admin

from apps.pedido_ambulatorio.models import Diagnostico, Practica_Medica, Pedido_Ambulatorio, Detalle_PedidoMedico

# Register your models here.
admin.site.register(Diagnostico)
admin.site.register(Practica_Medica)
admin.site.register(Pedido_Ambulatorio)
admin.site.register(Detalle_PedidoMedico)

# # Creamos el inline para el modelo Detalle_PedidoMedico
# class PedidoInline(admin.TabularInline):
#     model = Detalle_PedidoMedico
#     # Mostramos dos inlines vacíos por defecto
#     extra = 2
#
# class Pedido_AmbulatorioAdmin(admin.ModelAdmin):
#     list_display = ('idPedido', 'fecha_ingreso')
#     # Registramos el inline en el Pedido_Ambulatorio
#    inlines = [PedidoInline]