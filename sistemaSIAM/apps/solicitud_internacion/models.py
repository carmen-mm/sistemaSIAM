from django.db import models
from apps.beneficiario.models import Beneficiario
from apps.centromedico.models import CentroMedico
from apps.doctores.models import Doctor
from apps.pedido_ambulatorio.models import Diagnostico

# Create your models here.

class Internacion(models.Model):
    class Meta:
        db_table = 'Internación'
        verbose_name_plural = 'Internaciones'

    tipo1_CHOICES = (
        ('PISO', 'PISO'),
        ('TERAPIA', 'TERAPIA'),
        ('NEO', 'NEO'),
    )
    tipo2_CHOICES = (
        ('CLINICO', 'CLINICO'),
        ('QUIRURGICO', 'QUIRURGICO'),
    )

    #atributos propios
    fecha_ingreso = models.DateField()
    fecha_egreso = models.DateField(null=True, blank=True)
    dias_dados = models.IntegerField(null=True, blank=True)
    dias_prorroga = models.IntegerField(null=True, blank=True)
    tipo1_internacion = models.CharField(max_length=10, choices=tipo1_CHOICES)
    tipo2_internacion = models.CharField(max_length=10, choices=tipo2_CHOICES)

    #Relaciones
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    doctorTratante = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    centromedico = models.ForeignKey(CentroMedico, on_delete=models.CASCADE)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)
