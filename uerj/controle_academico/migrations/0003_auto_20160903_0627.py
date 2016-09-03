# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-03 06:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle_academico', '0002_auto_20160903_0601'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaCursada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(blank=True, null=True, verbose_name='Nota')),
                ('situacao', models.CharField(choices=[('IS', 'Inscri\xe7\xe3o Solicitada'), ('AC', 'Aceito'), ('AP', 'Aprovado'), ('RN', 'Reprovado por Nota'), ('AP', 'Reprovado por Faltas')], default='AC', max_length=2, verbose_name='Situa\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'Disciplina Cursada',
                'verbose_name_plural': 'Disciplinas Cursadas',
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(validators=[django.core.validators.MinValueValidator(2011)], verbose_name='Ano')),
                ('semestre', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)], verbose_name='Semestre')),
            ],
            options={
                'verbose_name': 'Per\xedodo',
                'verbose_name_plural': 'Per\xedodos',
            },
        ),
        migrations.AlterModelOptions(
            name='disciplina',
            options={'ordering': ('nome',), 'verbose_name': 'Disciplina', 'verbose_name_plural': 'Disciplinas'},
        ),
        migrations.AddField(
            model_name='disciplinacursada',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle_academico.Disciplina'),
        ),
        migrations.AddField(
            model_name='disciplinacursada',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle_academico.Periodo'),
        ),
    ]
