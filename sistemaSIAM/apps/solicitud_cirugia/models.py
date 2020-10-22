from django.db import models
from apps.beneficiario.models import Beneficiario
from apps.doctores.models import Doctor
from apps.centromedico.models import CentroMedico

from datetime import datetime

# Create your models here.

class Cirugia (models.Model):
    class Meta:
        db_table = 'Cirugia'
        verbose_name_plural = 'Cirugias'
    codigoCirugia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre


class Solicitud_Cirugia (models.Model):
    class Meta:
        db_table = 'Solicitud_cirugia'
        verbose_name_plural = 'Solicitud_de_cirugias'

    estado_CHOICES = (
        ('P', 'PENDIENTE',),
        ('R', 'RECHAZADA',),
        ('A', 'AUTORIZADA'),
    )
    tipo_CHOICES = (
        ('P', 'PROGRAMADA',),
        ('U', 'URGENCIA'),
    )
    #Atributos
    fecha_ingreso = models.DateField(default=datetime.now)
    estado_clave = models.CharField(max_length=1, choices=estado_CHOICES)
    material = models.BooleanField()
    prequirurgicos = models.BooleanField()
    fecha_cirugia = models.DateField(null=True, blank=True)
    tipo_cirugia = models.CharField(max_length=1, choices=tipo_CHOICES)
    importe_coseguro = models.FloatField(blank=True)
    observaciones = models.TextField(max_length=200)

    #Atributos - Relaciones
    #Una solicitud de cirugía corresponde a un beneficiario
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    # Una solicitud de Cirugía tiene una cirugía determinada
    cirugia = models.ForeignKey(Cirugia, on_delete=models.CASCADE)
    #Una solicitud de cirugía es solicitada por un Doctor tratante
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # Una solicitud de cirugía registra el Centro Médico donde se realiza la cirugía
    centromedico = models.ForeignKey(CentroMedico, on_delete=models.CASCADE)

