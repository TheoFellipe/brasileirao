from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from app.models import *
from django.views import View
from django.contrib import messages      

from app.models import Avaliacao
from app.forms import AvaliacaoForm

def avaliar(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('avaliar')  # Redireciona após a avaliação
    else:
        form = AvaliacaoForm()

    # Calcular a média das avaliações
    avaliacoes = Avaliacao.objects.all()
    media = avaliacoes.aggregate(models.Avg('nota'))['nota__avg'] or 0

    return render(request, 'avaliacao.html', {'form': form, 'media': media})

from django.shortcuts import render, redirect

def pagina_com_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_com_avaliacao')  # Redireciona após a avaliação
    else:
        form = AvaliacaoForm()

    # Calcular a média das avaliações
    avaliacoes = Avaliacao.objects.all()
    media = avaliacoes.aggregate(models.Avg('nota'))['nota__avg'] or 0

    return render(request, 'pagina.html', {'form': form, 'media': media})


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