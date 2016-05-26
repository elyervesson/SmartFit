"""Servidor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from SmartFit.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^auth_aluno/$', auth_aluno),
    url(r'^auth_instrutor/$', auth_instrutor),

    url(r'^aluno/(?P<id_aluno>\d+)/$', manipula_aluno),
    url(r'^aluno/$', cria_aluno),

    url(r'^instrutor/(?P<id_instrutor>\d+)/$', manipula_instrutor),
    url(r'^instrutor/$', cria_instrutor),

    url(r'^medida-aluno/(?P<id_medida>\d+)/$', manipula_medida_aluno_por_id_medida),
    url(r'^medida-aluno/$', cria_medida_aluno),

    url(r'^medidas-aluno/(?P<id_aluno>\d+)/$', recupera_medida_aluno_por_id_aluno),

    url(r'^exercicio/(?P<id_exercicio>\d+)/$', manipula_exercicio_por_id_exercicio),
    url(r'^exercicio/$', cria_exercicio),

    url(r'^descricao-exercicio/(?P<id_descricao>\d+)/$', manipula_descricao_exercicio_por_id_descricao),
    url(r'^descricao-exercicio/$', cria_descricao_exercicio),

    url(r'^treino/(?P<id_treino>\d+)/$', manipula_treino_por_id_treino),
    url(r'^treino/$', cria_treino),

    url(r'^treinos/(?P<id_aluno>\d+)/$', recupera_treino_por_id_aluno),
    url(r'^treinos/(?P<id_aluno>\d+)/(?P<dia>\d+)/$', recupera_treino_por_id_aluno_e_dia),

    # url(r'^ficha/(?P<id_ficha>\d+)/$', manipula_ficha_por_id_ficha),
    # url(r'^ficha/$', cria_ficha),
    #
    # url(r'^fichas/(?P<id_usuario>\d+)/$', recupera_ficha_por_id_usuario),

    # SEGUNDA OPCAO #
    url(r'^modo-execucao/(?P<id_modo_execucao>\d+)/$', manipula_modo_execucao_exercicio_por_id_modo_execucao),
    url(r'^modo-execucao/$', cria_modo_execucao_exercicio),

    url(r'^modo-execucao-com-exercicio/(?P<id_aluno>\d+)/(?P<dia>\d+)/$', recupera_modo_execucao_exercicio_por_id_aluno_e_dia),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
