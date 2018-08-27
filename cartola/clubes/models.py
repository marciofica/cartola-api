from django.db import models
from django.contrib.auth.models import User
from .utils import ChoiceEnum


class TipoGol(ChoiceEnum):
    AFAVOR = 'A'
    CONTRA = 'C'


class Clube(models.Model):
    nome = models.CharField(max_length=100)
    fundacao = models.DateField()

    class Meta:
        verbose_name = 'Clube'
        verbose_name_plural = 'Clubes'

    def __str__(self):
        return self.nome


class Time(models.Model):
    clube = models.ForeignKey(Clube, verbose_name='Clube', on_delete=models.PROTECT)
    nome = models.CharField(max_length=80)
    ano = models.IntegerField()
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'

    def __str__(self):
        return self.nome


class Jogador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    apelido = models.CharField(max_length=30)
    telefone = models.CharField(max_length=12, null=True)
    nota = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    posicao = models.CharField(max_length=2, null=True)
    numero_camisa = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'

    def __str__(self):
        return self.usuario.first_name + " " + self.usuario.last_name


class Indicador(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    ativo = models.CharField(max_length=1, default='S')

    class Meta:
        verbose_name = 'Indicador'
        verbose_name_plural = 'Indicadores'

    def __str__(self):
        return self.nome


class Partida(models.Model):
    dh_partida = models.DateTimeField()
    local = models.CharField(max_length=150)
    descricao = models.TextField()
    time1 = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='time1')
    time2 = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='time2')
    status = models.CharField(max_length=1)
    qtd_jogadores = models.IntegerField()

    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'

    def __str__(self):
        return self.descricao


class PartidaConfirmacao(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    dh_confirmacao = models.DateTimeField(auto_now_add=True)
    confirmado = models.CharField(max_length=1)

    class Meta:
        verbose_name = 'PartidaConfirmacao'
        verbose_name_plural = 'PartidasConfirmacoes'

    def __str__(self):
        return self.jogador.apelido


class PartidaGol(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    gols = models.IntegerField()
    tipo_gol = models.CharField(max_length=1, choices=TipoGol.choices(), default=TipoGol.AFAVOR)

    class Meta:
        verbose_name = 'PartidaGol'
        verbose_name_plural = 'PartidaGols'

    def __str__(self):
        return self.jogador.apelido


class PartidaIndicador(models.Model):
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    dh_votacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'PartidaIndicador'
        verbose_name_plural = 'PartidaIndicadores'

    def __str__(self):
        return self.gols + " - " + self.jogador.apelido


class PartidaNota(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    dh_votacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'PartidaNota'
        verbose_name_plural = 'PartidaNota'

    def __str__(self):
        return self.nota + " - " + self.jogador.apelido
