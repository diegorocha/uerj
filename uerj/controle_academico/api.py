# coding: utf-8
import models
import serializers
from rest_framework import viewsets
from django.shortcuts import render


class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = models.Unidade.objects.all()
    serializer_class = serializers.UnidadeSerializer


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = models.Disciplina.objects.all()
    serializer_class = serializers.DisciplinaSerializer


class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = models.Periodo.objects.all()
    serializer_class = serializers.PeriodoSerializer


class DisciplinaCursadaViewSet(viewsets.ModelViewSet):
    queryset = models.DisciplinaCursada.objects.all()
    serializer_class = serializers.DisciplinaCursadaSerializer


class HorarioViewSet(viewsets.ModelViewSet):
    queryset = models.Horario.objects.all()
    serializer_class = serializers.HorarioSerializer
