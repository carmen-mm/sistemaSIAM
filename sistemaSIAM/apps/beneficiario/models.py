from django.db import models
from apps.localidad_atencion.models import Localidad

# Modelo para la tabla Beneficiario:
# Un beneficiario es una persona que está empadronada correctamente en la obra social

class Beneficiario(models.Model):
    class Meta:
        db_table ='Beneficiarios'
        verbose_name_plural = 'Beneficiarios'
        ordering = ['-apellidos']
        #La dupla tipoDNI y dni debe ser única
        constraints = [
            models.UniqueConstraint(fields=['tipoDNI', 'dni'], name='documento')
        ]

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
    #Atributos
    tipoDNI = models.CharField(max_length=3, choices=tipoDNI_CHOICES)
    dni = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=30)
    afiliado = models.CharField(max_length=1, choices=AFILIADO_CHOICES)
    nroAfiliado = models.IntegerField(verbose_name='N° Afiliado', blank=True, null=True)

    #Relaciones
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        self.apellidos = (self.apellidos).upper()
        return super(Beneficiario, self).save(*args, **kwargs)

    def __str__(self):
      cadena = self.apellidos + " " + self.nombre + " - " + self.localidad.nombre
      return cadena

