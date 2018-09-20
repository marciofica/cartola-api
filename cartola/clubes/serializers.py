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

    def create(self, validated_data):
        print('usuario create')
        return self

    def update(self, instance, validated_data):
        print('update')
        return instance


class JogadorSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(required=True)

    class Meta:
        model = Jogador
        fields = ('id', 'usuario', 'apelido', 'telefone', 'nota', 'posicao', 'numero_camisa')

    def create(self, validated_data):
        user_data = validated_data.pop('usuario')
        usuario = UserSerializer.create(UserSerializer(), validated_data=user_data)

        jogador, created  = Jogador.objects.update_or_create(usuario=usuario,
                                                             apelido=validated_data.pop('apelido'),
                                                             telefone=validated_data.pop('telefone'),
                                                             nota=validated_data.pop('nota'),
                                                             posicao=validated_data.pop('posicao'),
                                                             numero_camisa=validated_data.pop('numero_camisa'))

        return jogador


class JogadorReadSerializer(JogadorSerializer):
    usuario = UserSerializer(read_only=True)


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
