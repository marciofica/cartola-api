from rest_framework import serializers
from .models import Clube, Time, Jogador, Partida, Indicador, PartidaConfirmacao, PartidaGol, PartidaIndicador, \
    PartidaNota
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


class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email')


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
