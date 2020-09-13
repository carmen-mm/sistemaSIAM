from django.db import models
from apps.localidad_atencion.models import Localidad
from apps.doctores.models import Especialidad, Doctor


# Create your models here.
# Modelo que contiene toda la información de los centro médicos que interactúan con la obra social.

class CentroMedico (models.Model):
    class Meta:
        db_table ='CentrosMedicos'
        verbose_name_plural='Centros médicos'
        ordering = ['-razonSocial']
    #Atributos
    razonSocial = models.CharField(max_length=150)
    domicilio = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
    horario = models.TextField(max_length=200)
    e_mail = models.EmailField(max_length=150)

    #Relaciones
    localidad = models.ForeignKey(Localidad, null=False, blank=False, on_delete=models.CASCADE)
    especialidades = models.ManyToManyField(Especialidad)
    doctores = models.ManyToManyField(Doctor, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.razonSocial = (self.razonSocial).upper()
        self.domicilio = (self.domicilio).upper()
        return super(CentroMedico, self).save(*args, **kwargs)

    def __str__(self):
        return self.razonSocial
















