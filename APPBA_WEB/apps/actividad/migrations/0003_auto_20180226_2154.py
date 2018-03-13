# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-27 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividad', '0002_auto_20180226_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='fecha_fina',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha De Culminacion'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='fecha_inic',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha De Inicio'),
        ),
    ]