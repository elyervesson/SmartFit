from django.contrib import admin

from .models import *

admin.site.register(Instrutor)
admin.site.register(Aluno)
admin.site.register(MedidaAluno)
admin.site.register(Exercicio)
admin.site.register(DescricaoExercicio)
admin.site.register(Treino)
# admin.site.register(Ficha)
admin.site.register(ModoExecucaoExercicio)

