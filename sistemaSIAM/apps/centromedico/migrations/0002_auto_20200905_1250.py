# Generated by Django 3.0.8 on 2020-09-05 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centromedico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centromedico',
            name='horario',
            field=models.TextField(max_length=200),
        ),
    ]