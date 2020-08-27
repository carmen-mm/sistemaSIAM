from django.db import models
from apps.localidad_atencion.models import Localidad

# Modelo para la tabla Beneficiario:
# Un beneficiario es una persona que está empadronada correctamente en la obra social

class Beneficiario(models.Model):
    AFILIADO_CHOICES = (
        ('S', 'AFILIADO'),
        ('N', 'NO AFILIADO'),
    )
    tipoDNI_CHOICES = (
        ('DNI', 'DNI'),
        ('LC', 'LC'),
        ('LE', 'LE'),
        ('S/D', 'S/D'),
    )

    tipoDNI = models.CharField(max_length=3, choices=tipoDNI_CHOICES)
    dni = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=30)
    afiliado = models.CharField(max_length=1, choices=AFILIADO_CHOICES)
    nroAfiliado = models.IntegerField(verbose_name='N° Afiliado', blank=True, null=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    class Meta:
        db_table ='Beneficiarios'
        verbose_name_plural = 'Beneficiarios'
        #unique_together = ("tipoDNI", "dni")
        constraints = [
            models.UniqueConstraint(fields=['tipoDNI', 'dni'], name='documento')
        ]
    def __str__(self):
      cadena = self.apellidos +" "+self.nombre
      return cadena

