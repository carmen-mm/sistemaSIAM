# Generated by Django 3.0.8 on 2020-09-10 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud_cirugia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cirugia',
            options={'verbose_name_plural': 'Cirugias'},
        ),
        migrations.AlterModelTable(
            name='cirugia',
            table='Cirugia',
        ),
    ]