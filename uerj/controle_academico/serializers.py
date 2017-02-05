from uerj.controle_academico import models
from rest_framework import serializers


class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unidade


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disciplina


class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Periodo


class DisciplinaCursadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DisciplinaCursada


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Horario
