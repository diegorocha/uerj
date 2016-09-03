# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_academico', '0008_horarioaula'),
    ]

    operations = [
        migrations.AddField(
            model_name='horarioaula',
            name='dia',
            field=models.IntegerField(choices=[(1, 'SEG'), (2, 'TER'), (3, 'QUA'), (4, 'QUI'), (5, 'SEX'), (6, 'SAB')], default=1, verbose_name='Dia'),
        ),
    ]
