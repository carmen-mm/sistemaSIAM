from django.db import models
#from apps.centromedico.models import CentroMedico

# Create your models here.
class Especialidad (models.Model):
    class Meta:
        db_table ='Especialidades'
        verbose_name_plural='Especialidades'
    idE = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre

class Doctor (models.Model):
    class Meta:
        db_table ='Doctores'
        verbose_name_plural='Doctores'
        ordering = ['-apellidos']
        constraints = [
            models.UniqueConstraint(fields=['matriculaMP', 'matriculaME'], name='matricula')
        ]
    convenio_CHOICES = (
        ('S', 'Con Convenio',),
        ('N', 'Sin Convenio',),)

    consultorio_CHOICES = (
        ('CP', 'consultorio propio',),
        ('CM', 'centro médico',),)

    #Atributos
    matriculaMP = models.IntegerField(verbose_name='Matrícula Provincial')
    matriculaME = models.IntegerField(verbose_name='Matrícula Especialidad', blank=True, null=True)
    cuit = models.CharField(primary_key=True, max_length=13, help_text='Ej:11-12345678-0')
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    trabaja_en = models.CharField(max_length=2, choices=consultorio_CHOICES)
    telefono = models.CharField(max_length=30, verbose_name='Teléfono', blank=True, null=True)
    domicilio = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=30, verbose_name='E-mail', help_text='Ej: hola@ejemplo.com', blank=True, null=True)
    convenioOSECAC = models.CharField(max_length=1, choices=convenio_CHOICES, blank=False, null=False)

    #Relaciones
    especialidad = models.ManyToManyField(Especialidad)


    def __str__(self):
        cadena = self.apellidos + " " + self.nombre
        return cadena



