# Generated by Django 3.0.8 on 2020-09-07 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Novedades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('titulo', models.CharField(max_length=150)),
                ('mensaje', models.TextField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Novedades',
                'db_table': 'Novedades',
                'ordering': ['fecha'],
            },
        ),
    ]