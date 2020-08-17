from django.db import models
from apps.localidad_atencion.models import Localidad
from apps.doctores.models import Especialidad


# Create your models here.
# Modelo que contiene toda la información de los centro médicos que interactúan con la obra social.

class CentroMedico (models.Model):
    class Meta:
        db_table ='Centros médicos'
        verbose_name_plural='Centros médicos'
    cuitCM = models.CharField(primary_key=True, max_length=13, help_text='Ej:12-34567890-0')
    localidad = models.ForeignKey(Localidad, null=False, blank=False, on_delete=models.CASCADE)
    razonSocial = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    horario = models.TextField(max_length=200)
    e_mail = models.EmailField(max_length=50)
#   especialidad = models.ManyToManyField(Especialidad)
#    doctores = models.ManyToManyField()

class CentroMedico_brinda_Especialidades(models.Model):
    class Meta:
        db_table ='CM_brinda_Especialidades'
        verbose_name_plural='Centros Médicos brinda Especialidades'
    centroMedico = models.ForeignKey(CentroMedico, on_delete=models.CASCADE)
    especialidades = models.ForeignKey(Especialidad, on_delete=models.CASCADE)