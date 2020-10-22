from django.db import models
from apps.beneficiario.models import Beneficiario
from apps.doctores.models import Doctor
from datetime import datetime


# Create your models here.

class Practica_Medica (models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    class Meta:
        db_table ='PracticasMedicas'   #nombre de la tabla en la BD
        verbose_name = 'Práctica médica'
        verbose_name_plural = 'Prácticas médicas'

    def __str__(self):
        return self.nombre

class Diagnostico (models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.TextField(max_length=250, default=' ')
    class Meta:
        db_table = 'Diagnostico'
        verbose_name_plural = 'Diagnósticos'
    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        return super(Diagnostico, self).save(*args, **kwargs)

    def __str__(self):
        cadena = self.codigo + "-" + self.nombre
        return cadena

# Un Pedido Ambulatorio contiene las prácticas ambulatorias que solicita/n uno o más doctores a un Beneficiario

class Pedido_Ambulatorio(models.Model):
    class Meta:
        db_table = 'PedidosAmbulatorios'
        verbose_name_plural = 'Pedidos ambulatorios'

    #Atributos del pedido
    idPedido = models.IntegerField()
    fecha_ingreso = models.DateField(default=datetime.now)

    # Relaciones
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)


class Detalle_PedidoMedico(models.Model):
    class Meta:
        db_table = 'DetallePedidoMedico'
        verbose_name_plural = 'Detalles'

    estado_CHOICES = (
            ('P', 'PENDIENTE',),
            ('R', 'RECHAZADO',),
            ('A', 'AUTORIZADO'),
        )
    autorizado = models.CharField(max_length=1, choices=estado_CHOICES)
    importeCoseguro = models.FloatField(blank=True, null=True, verbose_name='Importe Coseguro')
    observaciones = models.TextField(max_length=100, blank=True, null=True)

    #Relaciones
    pedido = models.ForeignKey(Pedido_Ambulatorio, on_delete=models.CASCADE)
    doctores = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    practicas = models.ForeignKey(Practica_Medica, on_delete=models.CASCADE)







