from django.db import models
from datetime import datetime

# Create your models here.
class Novedades(models.Model):
    class Meta:
        db_table ='Novedades'
        verbose_name_plural = 'Novedades'
        ordering = ['fecha']
    fecha = models.DateField(default=datetime.now)
    titulo = models.CharField(max_length=150)
    mensaje = models.TextField(max_length=250)

    def __str__(self):
        return self.titulo