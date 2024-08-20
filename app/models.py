from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome} {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupacao")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Pessoa")
    nome_do_pai = models.CharField(max_length=100, verbose_name="Nome do pai da Pessoa")
    nome_da_mae = models.CharField(max_length=100, verbose_name="Nome da mae da Pessoa")
    data_nasc = models.DateField(verbose_name="Data de nascimento da pessoa")
    email = models.CharField(max_length=100, verbose_name="Email da pessoa")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,verbose_name="Cidade da Pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE,verbose_name="Ocupacao da Pessoa")
    def __str__(self):
        return f"{self.nome} {self.nome_do_pai} {self.nome_da_mae} {self.data_nasc} {self.email} {self.cidade} {self.ocupacao}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class Time(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Time")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,verbose_name="Cidade do Time")
    tecnicoatual = models.ForeignKey(Pessoa, related_name='times_tecnicoanterior', on_delete=models.CASCADE,verbose_name="Tecnico atual do Time")
    tecncioanterior = models.ForeignKey(Pessoa, related_name='times_tecnicoatual', on_delete=models.CASCADE,verbose_name="Tecnico anterior do Time")
    def __str__(self):
        return f"{self.nome}, {self.cidade}, {self.tecnicoatual}, {self.tecncioanterior}"
    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"
        
class Uniforme(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE,verbose_name="Nome do Time")
    tipouni = models.CharField(max_length=100, verbose_name="Tipo do uniforme")
    def __str__(self):
        return f"{self.time}, {self.tipouni}"
    class Meta:
        verbose_name = "Uniforme"
        verbose_name_plural = "Uniformes"

class Campeonato(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Campeonato")
    ano = models.DateField(max_length=100, verbose_name="Ano do Campeonato")
    serie = models.CharField(max_length=1, verbose_name="Serie do Campeonato")
    def __str__(self):
        return f"{self.nome}, {self.ano},{self.serie}"
    class Meta:
        verbose_name = "Campeonato"
        verbose_name_plural = "Campeonatos"


class Partida(models.Model):
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE,verbose_name="Campeonato a ser disputado")
    time1 = models.ForeignKey(Time,related_name='partidas_time1', on_delete=models.CASCADE,verbose_name="Time mandante")
    time2 = models.ForeignKey(Time,related_name='partidas_time2', on_delete=models.CASCADE,verbose_name="Time Visitante")
    placar = models.CharField(max_length=100, verbose_name="Placar da partida")
    def __str__(self):
        return f"{self.campeonato}, {self.time1}, {self.time2}, {self.placar}"
    class Meta:
        verbose_name = "Partida"
        verbose_name_plural = "Partidas"

