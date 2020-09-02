from django.db import models
from apps.localidad_atencion.models import Localidad
from apps.doctores.models import Especialidad, Doctor


# Create your models here.
# Modelo que contiene toda la información de los centro médicos que interactúan con la obra social.

class CentroMedico (models.Model):
    class Meta:
        db_table ='Centros medicos'
        verbose_name_plural='Centros médicos'
    #cuitCM = models.CharField(primary_key=True, max_length=13, help_text='Ej:12-34567890-0')
    localidad = models.ForeignKey(Localidad, null=False, blank=False, on_delete=models.CASCADE)
    razonSocial = models.CharField(max_length=150)
    domicilio = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
   # horario = models.TextField(max_length=200)
    e_mail = models.EmailField(max_length=150)
    especialidades = models.ManyToManyField(Especialidad)
    doctores = models.ManyToManyField(Doctor)

    def __str__(self):
        return self.razonSocial
















