from django.db import models

# Create your models here.
class Especialidad (models.Model):
    class Meta:
        db_table ='Especialidades'
        verbose_name_plural='Especialidades'
    idE = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    #descripcion = models.TextField(max_length=200)

class Doctor (models.Model):
    class Meta:
        db_table ='Doctores'
        verbose_name_plural='Doctores'
    convenio_CHOICES = (
        ('S', 'Con Convenio',),
        ('N', 'Sin Convenio',),
    )
    matriculaDoc = models.IntegerField(verbose_name='Matrícula')
    cuit = models.CharField(primary_key=True, max_length=13, help_text='Ej:11-12345678-0')
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    especialidad = models.ManyToManyField(Especialidad, through='DoctorTieneEspecialidad')
    telefono = models.CharField(max_length=30, verbose_name='Teléfono')
    domicilio = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,verbose_name='E-mail', help_text='Ej: hola@ejemplo.com')
    convenioOSECAC = models.CharField(max_length=1, choices=convenio_CHOICES, blank=False, null=False)

class DoctorTieneEspecialidad (models.Model):
    class Meta:
        db_table ='DoctorTieneEspecialidades'
        verbose_name_plural='Doctor tiene Especialidades'
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    horario = models.CharField(max_length=250)





