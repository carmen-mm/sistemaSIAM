from django.contrib import admin
# from django.db.models import Max

from apps.pedido_ambulatorio.models import Diagnostico, Practica_Medica, Pedido_Ambulatorio, Detalle_PedidoMedico


# class Detalle_PedidoMedico_Admin(admin.ModelAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         form1 = super(Detalle_PedidoMedico_Admin, self).get_form(request, obj, **kwargs)
#
#         print("_____admin")
#
#         if obj is None:
#             max_pedido_ambulatorio = Detalle_PedidoMedico.objects.aggregate(Max('pedido__idPedido'))
#
#             print(max_pedido_ambulatorio['pedido__idPedido__max'])
#
#             if max_pedido_ambulatorio and max_pedido_ambulatorio['pedido__idPedido__max']:
#                 form1.base_fields['pedido__idPedido'].initial = max_pedido_ambulatorio['pedido__idPedido__max'] + 1
#             else:
#                 form1.base_fields['pedido__idPedido'].initial = 1
#         else:
#             form1.base_fields['pedido__idPedido'].widget.attrs['readonly'] = True
#         return form1


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
