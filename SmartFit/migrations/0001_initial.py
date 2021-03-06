# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 11:53
from __future__ import unicode_literals

import SmartFit.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=25, unique=True)),
                ('senha', models.CharField(max_length=80)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DescricaoExercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField(blank=True, null=True)),
                ('series', models.IntegerField(blank=True, null=True)),
                ('repeticoes', models.IntegerField(blank=True, null=True)),
                ('tempo_descanco', models.IntegerField(blank=True, null=True)),
                ('recomendacoes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('grupo_muscular', models.CharField(max_length=100)),
                ('url_imagem', models.ImageField(default='exercicio/no_image.jpg', upload_to=SmartFit.models.get_uplaod_file_name)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instrutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=25, unique=True)),
                ('senha', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='MedidaAluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('peso_total', models.FloatField(blank=True, null=True)),
                ('altura', models.FloatField(blank=True, null=True)),
                ('medida_braco_direito', models.FloatField(blank=True, null=True)),
                ('medida_braco_esquerdo', models.FloatField(blank=True, null=True)),
                ('medida_antebraco_direito', models.FloatField(blank=True, null=True)),
                ('medida_antebraco_esquerdo', models.FloatField(blank=True, null=True)),
                ('medida_ombro', models.FloatField(blank=True, null=True)),
                ('medida_torax', models.FloatField(blank=True, null=True)),
                ('medida_busto', models.FloatField(blank=True, null=True)),
                ('medida_abdomen', models.FloatField(blank=True, null=True)),
                ('medida_cintura', models.FloatField(blank=True, null=True)),
                ('medida_quadril', models.FloatField(blank=True, null=True)),
                ('medida_coxa_direita', models.FloatField(blank=True, null=True)),
                ('medida_coxa_esquerda', models.FloatField(blank=True, null=True)),
                ('medida_panturrilha_direita', models.FloatField(blank=True, null=True)),
                ('medida_panturrilha_esquerda', models.FloatField(blank=True, null=True)),
                ('medida_gordura', models.FloatField(blank=True, null=True)),
                ('medida_massa_magra', models.FloatField(blank=True, null=True)),
                ('data_medida', models.DateTimeField(auto_now_add=True)),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmartFit.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='ModoExecucaoExercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_do_exercicio', models.IntegerField()),
                ('peso', models.FloatField(blank=True, null=True)),
                ('series', models.IntegerField(blank=True, null=True)),
                ('repeticoes', models.IntegerField(blank=True, null=True)),
                ('tempo_descanco', models.IntegerField(blank=True, null=True)),
                ('recomendacoes', models.TextField(blank=True, null=True)),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmartFit.Aluno')),
                ('id_exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercicios', to='SmartFit.Exercicio')),
            ],
        ),
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.IntegerField()),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmartFit.Aluno')),
                ('id_exercicio_01', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
                ('id_exercicio_02', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
                ('id_exercicio_03', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
                ('id_exercicio_04', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
                ('id_exercicio_05', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
                ('id_exercicio_06', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
                ('id_exercicio_07', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
                ('id_exercicio_08', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
                ('id_exercicio_09', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
                ('id_exercicio_10', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
                ('id_exercicio_11', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
                ('id_exercicio_12', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='SmartFit.DescricaoExercicio')),
            ],
        ),
        migrations.AddField(
            model_name='descricaoexercicio',
            name='id_exercicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmartFit.Exercicio'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='id_instrutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SmartFit.Instrutor'),
        ),
    ]
