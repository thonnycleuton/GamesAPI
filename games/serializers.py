from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'game_category')

    # metodo responsavel por checar se o valor passado esta vazio
    def is_empty(self, value):
        if not value:
            raise serializers.ValidationError("Campo Requerido")
        return value

    # metodo responsavel por validacoes no campo release_date
    def validate_release_date(self, value):
        return self.is_empty(value)

    # metodo responsavel por validacoes no campo game_category
    def validate_game_category(self, value):
        return self.is_empty(value)

    # metodo responsavel por validacoes no campo name
    def validate_name(self, value):
        # checa se campo esta vazio
        self.is_empty(value)
        # checa se o nome ja nao consta resgistrado
        if Game.objects.filter(name__exact=value.upper()).exists():
            raise serializers.ValidationError("Nome de jogo ja registrado.")

        return self.is_empty(value)
