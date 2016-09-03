# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Unidade(models.Model):
    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        ordering = ('sigla', )
    sigla = models.CharField('Sigla', max_length=5)
    nome = models.CharField('Nome', max_length=50)

    def __unicode__(self):
        if self.sigla and self.nome:
            return '%s - %s' % (self.sigla, self.nome)
        return 'Unidade'


class Disciplina(models.Model):
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ('nome', )
    OBRIGATORIA = 'O'
    UNIVERSAL = 'U'
    ELETIVA = 'E'
    TIPO_CHOICES = (
        (OBRIGATORIA, 'Obrigatória'),
        (UNIVERSAL, 'Universal'),
        (ELETIVA, 'Eletiva'),
    )
    nome = models.CharField('Nome', max_length=100)
    unidade = models.ForeignKey(Unidade, related_name='disciplinas')
    departamento = models.IntegerField('Departamento')
    codigo = models.IntegerField('Código')
    creditos = models.IntegerField('Créditos')
    carga_horaria = models.IntegerField('Carga Horaria')
    carga_horaria_semanal = models.IntegerField('Carga Horaria Semanal')
    tipo = models.CharField('Tipo', max_length=1, choices=TIPO_CHOICES, default=UNIVERSAL)

    def __unicode__(self):
        return '%s %02d-%s %s' % (self.unidade.sigla, self.departamento, self.codigo, self.nome)


class Periodo(models.Model):
    class Meta:
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'
    ano = models.IntegerField('Ano', validators=[MinValueValidator(2011)])
    semestre = models.IntegerField('Semestre', validators=[MinValueValidator(1), MaxValueValidator(2)])
    atual = models.BooleanField('Atual', default=False)

    def __unicode__(self):
        return '%d/%d' % (self.ano, self.semestre)


class DisciplinaCursada(models.Model):
    class Meta:
        verbose_name = 'Disciplina Cursada'
        verbose_name_plural = 'Disciplinas Cursadas'
    SOLICITADO = 'IS'
    ACEITO = 'AC'
    APROVADO = 'AP'
    REPROVADO_NOTA = 'RN'
    REPROVADO_FALTAS = 'RF'
    SITUACAO_CHOICES = (
        (SOLICITADO, 'Inscrição Solicitada'),
        (ACEITO, 'Aceito'),
        (APROVADO, 'Aprovado'),
        (REPROVADO_NOTA, 'Reprovado por Nota'),
        (REPROVADO_FALTAS, 'Reprovado por Faltas'),
    )
    periodo = models.ForeignKey(Periodo)
    disciplina = models.ForeignKey(Disciplina)
    professor = models.CharField('Professor', max_length=100, null=True, blank=True)
    nota = models.FloatField('Nota', null=True, blank=True)
    situacao = models.CharField('Situação', max_length=2, choices=SITUACAO_CHOICES, default=ACEITO)

    def __unicode__(self):
        return '%s em %s' % (self.disciplina.nome, self.periodo)


class Horario(models.Model):
    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'
    sigla = models.CharField('Sigla', max_length=2)
    inicio = models.TimeField('Início')
    final = models.TimeField('Final')

    def __unicode__(self):
        return '%s [%s - %s]' % (self.sigla, self.inicio, self.final)


class HorarioAula(models.Model):
    class Meta:
        verbose_name = 'Horário Aula'
        verbose_name_plural = 'Horários Aulas'
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5
    SABADO = 6
    DIA_CHOICES = (
        (SEGUNDA, 'SEG'),
        (TERCA, 'TER'),
        (QUARTA, 'QUA'),
        (QUINTA, 'QUI'),
        (SEXTA, 'SEX'),
        (SABADO, 'SAB'),
    )
    disciplina_cursada = models.ForeignKey(DisciplinaCursada)
    dia = models.IntegerField('Dia', choices=DIA_CHOICES, default=1)
    horario_inicial = models.ForeignKey(Horario, related_name='horario_inicial')
    horario_final = models.ForeignKey(Horario, related_name='horario_final')
    sala = models.CharField('Sala', max_length=20, null=True, blank=True)

    def periodo(self):
        if self.disciplina_cursada:
            return self.disciplina_cursada.periodo

    def disciplina(self):
        if self.disciplina_cursada:
            return self.disciplina_cursada.disciplina.nome

    def professor(self):
        if self.disciplina_cursada:
            return self.disciplina_cursada.professor

    def inicio(self):
        if self.horario_inicial:
            return self.horario_inicial.inicio

    def final(self):
        if self.horario_final:
            return self.horario_final.final

    def __unicode__(self):
        return '%s as %s - %s' % (self.disciplina_cursada.disciplina.nome, self.dia, self.horario_inicial)
