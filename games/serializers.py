import datetime
from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Game, GameCategory, Score, Player


class GameSerializer(serializers.ModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')

    class Meta:
        model = Game
        fields = ('url', 'game_category', 'name', 'release_date', 'played',)

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


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameCategory
        fields = ('url', 'pk', 'name', 'games',)


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name')
    player = serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field='name')

    class Meta:
        model = Score
        fields = ('url', 'pk', 'score', 'score_date', 'player', 'game',)

    # metodo responsavel por checar se o valor passado esta vazio
    def is_empty(self, value):
        if not value:
            raise serializers.ValidationError("Campo Requerido")
        return value

    # metodo responsavel por validacoes no campo release_date
    def validate_player(self, value):
        return self.is_empty(value)

    # metodo responsavel por validacoes no campo game_category
    def validate_game(self, value):
        return self.is_empty(value)

    # metodo responsavel por validacoes no campo name
    def validate_score(self, value):

        self.is_empty(value)

        if value < 0:
            raise serializers.ValidationError("Valor do Score precisa ser maior que 0")

        return value

        # metodo responsavel por validacoes no campo name
    def validate_score_date(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Data nao pode ser superior ao dia atual")
        return value


class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ('url', 'name', 'gender', 'scores',)
