# coding: utf-8
import models
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class HorarioView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'horarios.html'

    def data(self):
        data = {}
        data['horarios'] = [{'dia': 'Seg', 'horarios': []},
                            {'dia': 'Ter', 'horarios': []},
                            {'dia': 'Qua', 'horarios': []},
                            {'dia': 'Qui', 'horarios': []},
                            {'dia': 'Sex', 'horarios': []},
                            {'dia': 'Sab', 'horarios': []},
                            ]
        periodo_atual = models.Periodo.objects.filter(atual=True).first()
        for horarios in models.HorarioAula.objects.filter(disciplina_cursada__periodo=periodo_atual).order_by('dia', 'horario_inicial'):
            data['horarios'][horarios.dia-1]['horarios'].append(horarios)
        data['periodo'] = periodo_atual
        return data


class HistoricoView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'historico.html'

    def data(self):
        data = {}
        data['periodos'] = models.Periodo.objects.all()
        data['disciplinas_cursadas'] = models.DisciplinaCursada.objects.all().order_by('periodo',)
        return data
