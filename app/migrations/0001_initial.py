# Generated by Django 5.0.7 on 2024-08-13 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Campeonato')),
                ('ano', models.DateField(max_length=100, verbose_name='Ano do Campeonato')),
                ('serie', models.CharField(max_length=1, verbose_name='Serie do Campeonato')),
            ],
            options={
                'verbose_name': 'Campeonato',
                'verbose_name_plural': 'Campeonatos',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Ocupacao')),
            ],
            options={
                'verbose_name': 'Ocupacao',
                'verbose_name_plural': 'Ocupacoes',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Pessoa')),
                ('nome_do_pai', models.CharField(max_length=100, verbose_name='Nome do pai da Pessoa')),
                ('nome_da_mae', models.CharField(max_length=100, verbose_name='Nome da mae da Pessoa')),
                ('data_nasc', models.DateField(verbose_name='Data de nascimento da pessoa')),
                ('email', models.CharField(max_length=100, verbose_name='Email da pessoa')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade da Pessoa')),
                ('ocupacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao', verbose_name='Ocupacao da Pessoa')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Time')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade do Time')),
                ('tecncioanterior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times_tecnicoatual', to='app.pessoa', verbose_name='Tecnico anterior do Time')),
                ('tecnicoatual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times_tecnicoanterior', to='app.pessoa', verbose_name='Tecnico atual do Time')),
            ],
            options={
                'verbose_name': 'Time',
                'verbose_name_plural': 'Times',
            },
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placar', models.CharField(max_length=100, verbose_name='Placar da partida')),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.campeonato', verbose_name='Campeonato a ser disputado')),
                ('time1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidas_time1', to='app.time', verbose_name='Time mandante')),
                ('time2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidas_time2', to='app.time', verbose_name='Time Visitante')),
            ],
            options={
                'verbose_name': 'Partida',
                'verbose_name_plural': 'Partidas',
            },
        ),
        migrations.CreateModel(
            name='Uniforme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipouni', models.CharField(max_length=100, verbose_name='Tipo do uniforme')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.time', verbose_name='Nome do Time')),
            ],
            options={
                'verbose_name': 'Uniforme',
                'verbose_name_plural': 'Uniformes',
            },
        ),
    ]
