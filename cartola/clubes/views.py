from rest_framework import viewsets

from .serializers import ClubeSerializer, TimeSerializer, UserSerializer, JogadorSerializer, PartidaSerializer, \
    IndicadorSerializer, PartidaConfirmacaoSerializer, PartidaGolSerializer, PartidaIndicadorSerializer, \
    PartidaNotaSerializer
from .models import Clube, Time, Jogador, Partida, Indicador, PartidaConfirmacao, PartidaGol, PartidaIndicador, \
    PartidaNota
from django.contrib.auth.models import User


class ClubeViewSet(viewsets.ModelViewSet):
    queryset = Clube.objects.all()
    serializer_class = ClubeSerializer


class TimeViewSet(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PartidaViewSet(viewsets.ModelViewSet):
    queryset = Partida.objects.all().order_by('-dh_partida')
    serializer_class = PartidaSerializer


class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer


class PartidaConfirmacaoViewSet(viewsets.ModelViewSet):
    queryset = PartidaConfirmacao.objects.all()
    serializer_class = PartidaConfirmacaoSerializer


class PartidaGolViewSet(viewsets.ModelViewSet):
    queryset = PartidaGol.objects.all()
    serializer_class = PartidaGolSerializer


class PartidaIndicadorViewSet(viewsets.ModelViewSet):
    queryset = PartidaIndicador.objects.all()
    serializer_class = PartidaIndicadorSerializer


class PartidaNotaViewSet(viewsets.ModelViewSet):
    queryset = PartidaNota.objects.all()
    serializer_class = PartidaNotaSerializer
