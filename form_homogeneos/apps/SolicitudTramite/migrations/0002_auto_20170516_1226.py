# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-16 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolicitudTramite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudtramite',
            name='cant_dias',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='solicitudtramite',
            name='fecha_solicitada',
            field=models.DateField(),
        ),
    ]
