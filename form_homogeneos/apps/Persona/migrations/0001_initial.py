# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-09 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cuil', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('legajo', models.CharField(blank=True, max_length=10, null=True)),
                ('subrogancia', models.NullBooleanField()),
                ('borrado', models.NullBooleanField()),
            ],
        ),
    ]
