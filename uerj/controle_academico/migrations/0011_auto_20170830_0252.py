# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-30 02:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_academico', '0010_auto_20160910_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodo',
            options={'ordering': ('ano', 'semestre'), 'verbose_name': 'Período', 'verbose_name_plural': 'Períodos'},
        ),
    ]
