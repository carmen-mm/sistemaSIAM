from django.db import models
from apps.localidad_atencion.models import Localidad

# Create your models here.
# Modelo para la tabla Beneficiario: Un beneficiario es una persona que está empadronada correctamente en la obra social
#class BeneficirioManager (models.Manager):
#    def beneficiario_exists(self, dni, tipoDNI):
#        return super(BeneficirioManager, self).get_queryset().filter(dni=dni, tipoDNI=tipoDNI).exists()


class Beneficiario(models.Model):
    AFILIADO_CHOICES = (
        ('S', 'AFILIADO'),
        ('N', 'NO AFILIADO'),
    )
    tipoDNI_CHOICES = (
        ('1', 'DNI'),
        ('2', 'LC'),
        ('3', 'LE'),
        ('4', 'S/D'),
    )

    tipoDNI = models.CharField(max_length=1, choices=tipoDNI_CHOICES)
    dni= models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    apellidos = models.CharField(max_length=30)
    afiliado = models.CharField(max_length=1, choices=AFILIADO_CHOICES)
    nroAfiliado = models.IntegerField(verbose_name='N° Afiliado', blank=True, null=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    class Meta:
        db_table ='Beneficiarios'
        unique_together = ("tipoDNI", "dni")
        verbose_name_plural = 'Beneficiarios'
    def __str__(self):
      cadena = self.apellidos +" "+self.nombre
      return cadena

''' def save(self, *args, **kwargs):
        if Beneficiario.beneficiario_exists(self.beneficiario.dni, self.beneficiario.tipoDNI):
            return "Este beneficiario ya existe"
        else:
            super(Beneficiario, self).save(*args, **kwargs)
'''