from rest_framework import serializers
from .models import Clube, Time, Jogador, Partida, Indicador, PartidaConfirmacao, PartidaGol, PartidaIndicador, \
    PartidaNota, JogadorClube
from django.contrib.auth.models import User


class ClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clube
        fields = ('id', 'nome', 'fundacao')

    def create(self, validated_data):
        clube = super().create(validated_data)
        clube.usuario = self.context['request'].user
        clube.save()
        return clube


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('id', 'clube', 'ano', 'nome', 'ativo')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'email')


class JogadorSerializer(serializers.ModelSerializer):
    apelido = serializers.CharField(source='jogador.apelido')
    telefone = serializers.CharField(source='jogador.telefone')
    nota = serializers.DecimalField(max_digits=4, decimal_places=2, source='jogador.nota')
    posicao = serializers.CharField(source='jogador.posicao')
    numero_camisa = serializers.IntegerField(source='jogador.numero_camisa')
    clube_id = serializers.IntegerField(source='clube.id')
    mensalista = serializers.BooleanField(source='clube.mensalista')

    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'email', 'apelido', 'telefone', 'nota', 'posicao', 'numero_camisa', 'clube_id', 'mensalista')

    def save(self, **kwargs):
        jogador = self.validated_data.pop('jogador')
        clube = self.validated_data.pop('clube')
        instance = super().save(**kwargs)
        clubeModel = Clube.objects.get(pk=clube['id'])
        jogadorModel, create = Jogador.objects.update_or_create(usuario=instance, defaults=jogador)
        jogadorClube = JogadorClube.objects.update_or_create(jogador=jogadorModel, clube=clubeModel, defaults=clube)
        return instance


class JogadorClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JogadorClube
        fields = '__all__'


class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = '__all__'


class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        fields = '__all__'


class PartidaConfirmacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidaConfirmacao
        fields = '__all__'


class PartidaGolSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidaGol
        fields = '__all__'


class PartidaIndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidaIndicador
        fields = '__all__'


class PartidaNotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidaNota
        fields = '__all__'


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
