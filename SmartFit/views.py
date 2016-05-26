from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .serializer import *
from .models import *


@api_view(['POST'])
def auth_aluno(request):
    aluno = get_object_or_404(Aluno, matricula=request.data['matricula'])
    result = {}
    if aluno.senha == request.data['senha']:
        result['result'] = True
        result['id'] = aluno.id
    else:
        result['result'] = False
        result['id'] = None
    return Response(result)


@api_view(['GET', 'PUT'])
def manipula_aluno(request, id_aluno):
    if request.method == 'GET':
        aluno = Aluno.objects.get(pk=id_aluno)
        serializer = AlunoSerializer(aluno, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        aluno = Aluno.objects.get(pk=id_aluno)
        serializer = AlunoSerializer(instance=aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def cria_aluno(request):
    serializer = AlunoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        aluno = Aluno.objects.get(matricula=request.data['matricula'])
        return Response(status=201, data={'id': aluno.id})
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def auth_instrutor(request):
    instrutor = get_object_or_404(Instrutor, matricula=request.data['matricula'])
    result = {}
    if instrutor.senha == request.data['senha']:
        result['result'] = True
        result['id'] = instrutor.id
    else:
        result['result'] = False
        result['id'] = None
    return Response(result)


@api_view(['GET', 'PUT'])
def manipula_instrutor(request, id_instrutor):
    if request.method == 'GET':
        instrutor = Instrutor.objects.get(pk=id_instrutor)
        serializer = InstrutorSerializer(instrutor, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        instrutor = Instrutor.objects.get(pk=id_instrutor)
        serializer = InstrutorSerializer(instance=instrutor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def cria_instrutor(request):
    serializer = InstrutorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        instrutor = Instrutor.objects.get(matricula=request.data['matricula'])
        return Response(status=201, data={'id': instrutor.id})
    return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT'])
def manipula_medida_aluno_por_id_medida(request, id_medida):
    if request.method == 'GET':
        medida_aluno = MedidaAluno.objects.get(pk=id_medida)
        serializer = MedidaAlunoSerializer(medida_aluno, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        medida_aluno = MedidaAluno.objects.get(pk=id_medida)
        serializer = InstrutorSerializer(instance=medida_aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def recupera_medida_aluno_por_id_aluno(request, id_aluno):
    if request.method == 'GET':
        medidas_aluno = MedidaAluno.objects.filter(id_aluno=id_aluno)
        print medidas_aluno
        serializer = MedidaAlunoSerializer(medidas_aluno, many=True)
        return Response(serializer.data)
    return Response(status=400)


@api_view(['POST'])
def cria_medida_aluno(request):
    serializer = MedidaAlunoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT'])
def manipula_exercicio_por_id_exercicio(request, id_exercicio):
    if request.method == 'GET':
        exercicio = Exercicio.objects.get(pk=id_exercicio)
        serializer = ExercicioSerializer(exercicio, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        exercicio = Exercicio.objects.get(pk=id_exercicio)
        serializer = ExercicioSerializer(instance=exercicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def cria_exercicio(request):
    serializer = ExercicioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT'])
def manipula_descricao_exercicio_por_id_descricao(request, id_descricao):
    if request.method == 'GET':
        descricao_exercicio = DescricaoExercicio.objects.get(pk=id_descricao)
        serializer = DescricaoExercicioSerializer(descricao_exercicio, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        descricao_exercicio = DescricaoExercicio.objects.get(pk=id_descricao)
        serializer = DescricaoExercicioSerializer(instance=descricao_exercicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def cria_descricao_exercicio(request):
    serializer = DescricaoExercicioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT'])
def manipula_treino_por_id_treino(request, id_treino):
    if request.method == 'GET':
        treino = Treino.objects.get(pk=id_treino)
        serializer = TreinoSerializer(treino, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        treino = Treino.objects.get(pk=id_treino)
        serializer = TreinoSerializer(instance=treino, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def cria_treino(request):
    serializer = TreinoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def recupera_treino_por_id_aluno(request, id_aluno):
    if request.method == 'GET':
        treinos = Treino.objects.filter(id_aluno=id_aluno)
        serializer = TreinoSerializer(treinos, many=True)
        return Response(serializer.data)
    return Response(status=400)


@api_view(['GET'])
def recupera_treino_por_id_aluno_e_dia(request, id_aluno, dia):
    if request.method == 'GET':
        treinos = Treino.objects.filter(id_aluno=id_aluno, dia=dia)
        serializer = TreinoSerializer(treinos, many=True)
        return Response(serializer.data)
    return Response(status=400)


# @api_view(['GET', 'PUT'])
# def manipula_ficha_por_id_ficha(request, id_ficha):
#     if request.method == 'GET':
#         ficha = Ficha.objects.get(pk=id_ficha)
#         serializer = FichaSerializer(ficha, many=False)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         ficha = Ficha.objects.get(pk=id_ficha)
#         serializer = FichaSerializer(instance=ficha, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=201)
#         return Response(serializer.errors, status=400)
#
#
# @api_view(['GET'])
# def recupera_ficha_por_id_usuario(request, id_usuario):
#     if request.method == 'GET':
#         ficha = Ficha.objects.filter(id_aluno=id_usuario)
#         serializer = FichaSerializer(ficha, many=True)
#         return Response(serializer.data)
#     return Response(status=400)
#
#
# @api_view(['POST'])
# def cria_ficha(request):
#     serializer = FichaSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(status=201)
#     return Response(serializer.errors, status=400)

# SEGUNDA OPCAO # ModoExecucaoExercicioSerializer

@api_view(['GET', 'PUT'])
def manipula_modo_execucao_exercicio_por_id_modo_execucao(request, id_modo_execucao):
    if request.method == 'GET':
        modo_execucao = ModoExecucaoExercicio.objects.get(pk=id_modo_execucao)
        serializer = ModoExecucaoExercicioSerializer(modo_execucao, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        modo_execucao = ModoExecucaoExercicio.objects.get(pk=id_modo_execucao)
        serializer = ModoExecucaoExercicioSerializer(instance=modo_execucao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def cria_modo_execucao_exercicio(request):
    serializer = ModoExecucaoExercicioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def recupera_modo_execucao_exercicio_por_id_aluno_e_dia(request, id_aluno, dia):
    if request.method == 'GET':
        try:
            modo_execucoes = ModoExecucaoExercicio.objects.get(id_aluno=id_aluno, dia_do_exercicio=dia)
            serializer = ModoExecucaoExercicioSerializer(modo_execucoes, many=False)
            exercicio = Exercicio.objects.get(pk=modo_execucoes.id_exercicio.id)
            serializer_exercicio = ExercicioSerializer(exercicio, many=False)

            data = {'exercicio': serializer_exercicio.data, 'modo_execucao': serializer.data}
        except:
            data = {'exercicio': None, 'modo_execucao': None}

        return Response(data)
    return Response(status=400)
