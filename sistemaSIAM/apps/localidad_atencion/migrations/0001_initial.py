# Generated by Django 3.0.8 on 2020-09-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('codigopostal', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Localidades',
                'db_table': 'Localidades',
            },
        ),
    ]
