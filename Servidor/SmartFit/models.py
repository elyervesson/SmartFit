# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Instrutor(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=25, unique=True)
    senha = models.CharField(max_length=80)

    def __unicode__(self):
        return u'Instrutor: %s' % self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=25, unique=True)
    senha = models.CharField(max_length=80)
    data_cadastrado = models.DateTimeField(auto_now_add=True)

    id_instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'Aluno: %s' % self.nome


class MedidaAluno(models.Model):
    peso_total = models.FloatField(blank=True, null=True)
    medida_abdomen = models.FloatField(blank=True, null=True)
    medida_antebraco_direito = models.FloatField(blank=True, null=True)
    medida_antebraco_esquerdo = models.FloatField(blank=True, null=True)
    medida_braco_direito = models.FloatField(blank=True, null=True)
    medida_braco_esquerdo = models.FloatField(blank=True, null=True)
    medida_busto = models.FloatField(blank=True, null=True)
    medida_cintura = models.FloatField(blank=True, null=True)
    medida_coxa_direita = models.FloatField(blank=True, null=True)
    medida_coxa_esquerda = models.FloatField(blank=True, null=True)
    medida_ombro = models.FloatField(blank=True, null=True)
    medida_perna_direita = models.FloatField(blank=True, null=True)
    medida_perna_esquerda = models.FloatField(blank=True, null=True)
    medida_quadril = models.FloatField(blank=True, null=True)
    medida_torax = models.FloatField(blank=True, null=True)
    data_medida = models.DateTimeField(auto_now_add=True)

    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'Medidas do aluno: %s' % self.id_aluno.nome

def get_uplaod_file_name(instance, filename):
    return 'exercicio/{0}'.format(filename)


class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    url_imagem = models.ImageField(upload_to=get_uplaod_file_name, default='exercicio/no_image.jpg')
    descricao = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'Exercicio: %s' % self.nome


class DescricaoExercicio(models.Model):
    peso = models.FloatField(blank=True, null=True)
    series = models.IntegerField(blank=True, null=True)
    repeticoes = models.IntegerField(blank=True, null=True)
    tempo_descanco = models.IntegerField(blank=True, null=True)  # Em segundos
    recomendacoes = models.TextField(blank=True, null=True)

    id_exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'Descrição especifica do exercicio: %s' % self.id_exercicio.nome


# Atualmente é possivel cadastrar ate 10 exercicios para cada dia de treino
class Treino(models.Model):
    dia = models.CharField(max_length=100)  # Talvez seja necessario alterar para DateField

    id_exercicio_01 = models.ForeignKey(DescricaoExercicio, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    id_exercicio_02 = models.ForeignKey(DescricaoExercicio, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    id_exercicio_03 = models.ForeignKey(DescricaoExercicio, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    id_exercicio_04 = models.ForeignKey(DescricaoExercicio, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    id_exercicio_05 = models.ForeignKey(DescricaoExercicio, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    id_exercicio_06 = models.ForeignKey(DescricaoExercicio, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    id_exercicio_07 = models.ForeignKey(DescricaoExercicio, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    id_exercicio_08 = models.ForeignKey(DescricaoExercicio, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    id_exercicio_09 = models.ForeignKey(DescricaoExercicio, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    id_exercicio_10 = models.ForeignKey(DescricaoExercicio, on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    def __unicode__(self):
        return u'Treino do dia: %s' % self.dia


class Ficha(models.Model):
    id_treino_01 = models.ForeignKey(Treino, blank=True, null=True, related_name='+')
    id_treino_02 = models.ForeignKey(Treino, blank=True, null=True, related_name='+')
    id_treino_03 = models.ForeignKey(Treino, blank=True, null=True, related_name='+')
    id_treino_04 = models.ForeignKey(Treino, blank=True, null=True, related_name='+')
    id_treino_05 = models.ForeignKey(Treino, blank=True, null=True, related_name='+')
    id_treino_06 = models.ForeignKey(Treino, blank=True, null=True, related_name='+')
    id_treino_07 = models.ForeignKey(Treino, blank=True, null=True, related_name='+')
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'Ficha do aluno: %s' % self.id_aluno.nome
