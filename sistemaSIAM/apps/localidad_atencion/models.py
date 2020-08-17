from django.db import models

# Create your models here.
# Modelo para la tabla Localidad de Atención médica

class Localidad(models.Model):
    codigopostal = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    class Meta:
        db_table ='Localidades'
        verbose_name_plural ='Localidades'
    def __str__(self):
      return self.nombre