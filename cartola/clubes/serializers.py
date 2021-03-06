from rest_framework import serializers
from .models import Clube, Time, Jogador, Partida, Indicador, PartidaConfirmacao, PartidaGol, PartidaIndicador, \
    PartidaNota, JogadorClube
from django.contrib.auth.models import User


class ClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clube
        fields = ('id', 'nome', 'fundacao')

    def create(self, validated_data):
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)


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
    data_nascimento = serializers.DateField(source='jogador.data_nascimento')

    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'email', 'apelido', 'telefone', 'data_nascimento')

    def save(self, **kwargs):
        jogador = self.validated_data.pop('jogador')
        instance = super().save(**kwargs)
        jogadorModel, create = Jogador.objects.update_or_create(usuario=instance, defaults=jogador)
        return instance


class JogadorClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JogadorClube
        fields = '__all__'


class JogadorSerializer2(serializers.ModelSerializer):
    jogadorClube = JogadorClubeSerializer(read_only=True)

    class Meta:
        model = Jogador
        fields = ('id', 'usuario', 'apelido', 'telefone', 'data_nascimento', 'jogadorClube')


class JogadorClubeReadSerializer(JogadorClubeSerializer):
    usuario = JogadorSerializer(read_only=True)
    clube = ClubeSerializer(read_only=True)


class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = '__all__'

    def create(self, validated_data):
        partida = super().create(validated_data)
        jogadores = JogadorClube.objects.filter(clube=partida.clube)

        for jogadorItem in jogadores:
            jogadorDb = Jogador.objects.get(usuario=jogadorItem.usuario)
            j = PartidaConfirmacao(partida=partida, jogador=jogadorDb, dh_confirmacao=None, confirmado=None)
            j.save()

        return partida


class PartidaReadSerializer(PartidaSerializer):
    time1 = TimeSerializer(read_only=True)
    time2 = TimeSerializer(read_only=True)


class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        fields = '__all__'


class PartidaConfirmacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidaConfirmacao
        fields = ('id', 'jogador', 'partida', 'dh_confirmacao', 'confirmado',)


class PartidaConfirmacaoReadSerializer(PartidaConfirmacaoSerializer):
    jogador = JogadorSerializer2(read_only=True)


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
