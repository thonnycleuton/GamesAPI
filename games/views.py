from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse

from games.models import Game, GameCategory, Player, Score
from games.serializers import GameSerializer, GameCategorySerializer, ScoreSerializer, PlayerSerializer


class GameCategoyViewSet(viewsets.ViewSet):

    # Required for the Browsable API renderer to have a nice form.

    queryset = GameCategory.objects.all()

    def list(self, request):
        serializer = GameCategorySerializer(self.queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        category = get_object_or_404(self.queryset, pk=pk)
        serializer = GameCategorySerializer(category, context={'request': request})
        return Response(serializer.data)


class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'


class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-list'


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    name = 'score-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'players': reverse(PlayerList.name, request=request),
                         'game-categories': reverse(GameCategoryList.name, request=request),
                         'games': reverse(GameList.name, request=request),
                         'scores': reverse(ScoreList.name, request=request)
                         })
