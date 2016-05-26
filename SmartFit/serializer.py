from rest_framework import serializers

from .models import *


class InstrutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrutor


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno


class MedidaAlunoSerializer(serializers.ModelSerializer):
    data_medida = serializers.DateTimeField(read_only=True)

    class Meta:
        model = MedidaAluno


class ExercicioSerializer(serializers.ModelSerializer):
    url_imagem = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Exercicio


class DescricaoExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescricaoExercicio


class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treino


# class FichaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ficha

# SEGUNDA OPCAO #

class ModoExecucaoExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModoExecucaoExercicio