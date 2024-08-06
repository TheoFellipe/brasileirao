from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages      




class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass
class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})
class TimesView(View):
    def get(self, request, *args, **kwargs):
        times = Time.objects.all()
        return render(request, 'time.html', {'time': times })
class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        Ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes':Ocupacoes})
class UniformesView(View):
    def get(self, request, *args, **kwargs):
        Uniformes = Uniforme.objects.all()
        return render(request, 'uniforme.html', {'uniformes': Uniformes})
class PessoasView(View):
    def get(self, request, *args, **kwargs):
        Pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': Pessoas})
class CampeonatosView(View):
    def get(self, request, *args, **kwargs):
        Campeonatos = Campeonato.objects.all()
        return render(request, 'campeonato.html', {'campeonatos': Campeonatos})
class PartidasView(View):
    def get(self, request, *args, **kwargs):
        Partidas = Partida.objects.all()
        return render(request, 'partida.html', {'partidas': Partidas})