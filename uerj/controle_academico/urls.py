import api
import views
from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'unidade', api.UnidadeViewSet)
router.register(r'disciplina', api.DisciplinaViewSet)
router.register(r'periodo', api.PeriodoViewSet)
router.register(r'disciplina_cursada', api.DisciplinaCursadaViewSet)
router.register(r'horario', api.HorarioViewSet)

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^horarios/$', views.HorarioView.as_view(), name='horarios'),
    url(r'^historico/$', views.HistoricoView.as_view(), name='historico'),
    url(r'^a-cursar/$', views.DisciplinasACursarView.as_view(), name='a-cursar'),
    url(r'^api/', include(router.urls, namespace='api')),
]
