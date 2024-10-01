from django.contrib import admin
from .models import *
from django.contrib import admin

admin.site.register(Cidade)

admin.site.register(Time)
admin.site.register(Uniforme)
admin.site.register(Pessoa)
admin.site.register(Campeonato)
admin.site.register(Partida)

class  PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1 # Número de livros adicionais para adicionar no admin

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)# Campos que serão exibidos na listagem
    search_fields = ('nome',)# Campos que serão pesquisado
    inlines = [PessoaInline]# Adiciona a tabela de livros no admin de gêneros
admin.site.register(Ocupacao,OcupacaoAdmin)