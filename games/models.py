from django.db import models

from games.utils import Genero


class GameCategory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


# Create your models here.
class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    release_date = models.DateTimeField(null=True)
    game_category = models.ForeignKey(GameCategory, related_name='games', on_delete=models.CASCADE)
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # este bloco implementa funcao para salvar em Caixa Alta antes de salvar
        for field_name in ['name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())
        super(Game, self).save(*args, **kwargs)


class Player(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=2, choices=Genero.choices(), default=Genero.MALE,)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Score(models.Model):
    player = models.ForeignKey(Player, related_name='scores', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()
    score_date = models.DateTimeField()

    class Meta:
        ordering = ('-score',)

    def __str__(self):
        return self.score
