# Generated by Django 3.0.8 on 2020-09-05 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beneficiario',
            options={'ordering': ['-apellidos'], 'verbose_name_plural': 'Beneficiarios'},
        ),
    ]