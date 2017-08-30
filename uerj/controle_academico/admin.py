from django.contrib import admin
from uerj.controle_academico import models


class HorarioAulaInline(admin.TabularInline):
    model = models.HorarioAula
    extra = 0


@admin.register(models.Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'atual']


@admin.register(models.DisciplinaCursada)
class DisciplinaCursadaAdmin(admin.ModelAdmin):
    list_display = ['periodo', 'disciplina', 'professor', 'nota', 'situacao']
    list_filter = ['periodo', 'situacao']
    inlines = (HorarioAulaInline, )


@admin.register(models.Horario)
class HorarioAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HorarioAula)
class HorarioAulaAdmin(admin.ModelAdmin):
    list_display = ['periodo', 'dia', 'inicio', 'final', 'disciplina', 'professor', 'sala']
