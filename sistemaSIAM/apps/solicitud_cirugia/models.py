'''
from django.db import models
from apps.beneficiario.models import Beneficiario
from apps.doctores.models import Doctor
from apps.centro_medico.models import CentroMedico
from apps.pedido_ambulatorio.models import Diagnostico
from datetime import datetime

# Create your models here.

#class Cirugia (models.Model):
    codigoCirugia = models.IntegerField(null=False, blank=False)
    nombre = models.CharField(max_length=50)
    importeTotal = models.FloatField(null=False, blank=False)
    descripcion = models.TextField(max_length=200)


#class Solicitud_Cirugia (models.Model):
    estado_CHOICES(
        ('P', 'PENDIENTE',),
        ('R', 'RECHAZADA',),
        ('A', 'AUTORIZADA'),
    )
    tipo_CHOICES(
        ('P', 'PROGRAMADA',),
        ('U', 'URGENCIA'),
    )
    beneficiario = models.ForeignKey(Beneficiario)
    fecha_ingreso = models.DateField(default=datetime.now, null=False, blank=False)
    fecha_prescripcion = models.DateField()
    # Una solicitud de Cirugía tiene una cirugía determinada
    cirugia = models.ForeignKey(Cirugia, null=False, blank=False, on_delete=models.CASCADE)

    # En una solicitud de cirugía intervienen varios doctores
    doctores = models.ManyToManyField(Doctor)

    # Una solicitud de cirugía registra el Centro Médico donde se realiza la cirugía
    centro_medico = models.ForeignKey(CentroMedico, null=False, blank=False, on_delete=models.CASCADE)

    # Una solicitud de cirugía tiene un diagnóstico
    diagnostico = models.ForeignKey(Diagnostico, null=False, blank=False, on_delete=models.CASCADE)

    estado_Clave = models.CharField(max_length=1, choices=estado_CHOICES, blank=False, null=False)
    material = models.BooleanField()
    prequirgicos = models.BooleanField()
    fecha_Cirugia = models.DateField(blank=True)
    tipo_Cirugia = models.CharField(max_length=1, choices=tipo_CHOICES, blank=False, null=False)
    importe_Coseguro = models.FloatField(blank=True)
    observaciones = models.TextField(max_length=200) '''