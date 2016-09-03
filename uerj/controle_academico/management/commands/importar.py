# coding: utf-8
import requests
import psycopg2
from django.core.management.base import BaseCommand, CommandError
from uerj.controle_academico import models


class Command(BaseCommand):
    help = 'Importa dados do sistema atual'

    def getDB(self):
        return psycopg2.connect("dbname='uerj' user='diego' host='postgres.cet1knx538vx.sa-east-1.rds.amazonaws.com' password='64n1m3d35'")

    def handle(self, *args, **options):
        dias = {'SEG': 1, 'TER': 2, 'QUA': 3, 'QUI': 4, 'SEX': 5, 'SÁB': 6}
        con = self.getDB()
        cursor = con.cursor()
        for periodo in models.Periodo.objects.order_by('ano', 'semestre'):
            sql = "select codDia, min(codTempo), max(codTempo), min(inicio) as inicio, max(fim) as fim, codDisciplina, sala from vwHorarioDisciplina where codPeriodo = '%d.%d' group by codDisciplina,disciplina,professor, codDia, sala order by codDia, inicio, fim;" % (periodo.ano, periodo.semestre)
            cursor.execute(sql)
            for r in cursor.fetchall():
                horario_aula = models.HorarioAula()
                horario_aula.dia = dias.get(r[0]) if r[0] in dias else 6
                horario_aula.disciplina_cursada = models.DisciplinaCursada.objects.get(periodo__pk=periodo.pk, disciplina__codigo=r[5])
                horario_aula.horario_inicial = models.Horario.objects.get(sigla=r[1])
                horario_aula.horario_final = models.Horario.objects.get(sigla=r[2])
                horario_aula.sala = r[6]
                horario_aula.save()
                print horario_aula.disciplina_cursada
