# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-12 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tramite', '0002_auto_20170512_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipotramite',
            name='tipo_exp',
        ),
        migrations.AddField(
            model_name='tipotramite',
            name='tramite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tramite.Tramite'),
        ),
        migrations.AlterField(
            model_name='tipotramite',
            name='tipo_tramite',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
