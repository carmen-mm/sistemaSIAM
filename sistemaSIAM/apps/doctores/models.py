from django.db import models


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
        ('SI', 'Con Convenio',),
        ('NO', 'Sin Convenio',),)


    #Atributos
    matriculaMP = models.IntegerField(verbose_name='Matrícula Provincial')
    matriculaME = models.IntegerField(verbose_name='Matrícula Especialidad', blank=True, null=True)
    cuit = models.CharField(primary_key=True, max_length=13, help_text='Ej:11-12345678-0')
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    convenioOSECAC = models.CharField(max_length=2, choices=convenio_CHOICES)

    #Relaciones
    especialidad = models.ManyToManyField(Especialidad)

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        self.apellidos = (self.apellidos).upper()
        return super(Doctor, self).save(*args, **kwargs)
    def __str__(self):
        cadena = self.apellidos + " " + self.nombre
        return cadena



