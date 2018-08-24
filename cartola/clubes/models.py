from django.db import models
from django.contrib.auth.models import User


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
        return self.usuario.fisrt_name
