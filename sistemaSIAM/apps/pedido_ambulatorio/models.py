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

    def __str__(self):
        cadena = self.codigo + "-" + self.nombre
        return cadena

# Un Pedido Ambulatorio contiene las prácticas ambulatorias que solicita/n uno o más doctores a un Beneficiario
'''
class Pedido_Ambulatorio(models.Model):
    class Meta:
        db_table = 'PedidosAmbulatorios'
        verbose_name_plural = 'Pedidos ambulatorios'
        
    estado_CHOICES = (
        ('P', 'PENDIENTE',),
        ('R', 'RECHAZADO',),
        ('A', 'AUTORIZADO'),
    )
    #Atributos del pedido
    idPedido = models.IntegerField(primary_key=True, default=None)
    fecha_ingreso = models.DateField(default=datetime.now)
    fecha_prescripcion = models.DateField()
    autorizado = models.CharField(max_length=1, choices= estado_CHOICES)

    #Relaciones
    # Un Pedido Ambulatorio pertenece a un Beneficiario
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)

    # Un Pedido Ambulatorio puede tener muchos Doctores
    doctores = models.ManyToManyField(Doctor, on_delete=models.CASCADE)

    # Un Pedido Ambulatorio puede tener muchos Diagnosticos
    diagnosticos = models.ManyToManyField(Diagnostico, on_delete=models.CASCADE)

    # Un Pedido Ambulatorio puede tener muchas Practicas médicas
    practicas = models.ManyToManyField(Practica_Medica, on_delete=models.CASCADE)

    importeCoseguro = models.FloatField(blank=True, null=True, verbose_name='Importe Coseguro')
    observaciones = models.TextField(max_length=200, blank=True, null=True)

'''
