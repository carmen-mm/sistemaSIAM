# Generated by Django 3.0.8 on 2020-10-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiario',
            name='afiliado',
            field=models.CharField(choices=[('SI', 'AFILIADO'), ('NO', 'NO AFILIADO')], max_length=2),
        ),
    ]