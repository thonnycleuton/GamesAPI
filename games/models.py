from django.db import models


# Create your models here.
class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    release_date = models.DateTimeField(null=True)
    game_category = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        # este bloco implementa funcao para salvar em Caixa Alta antes de salvar
        for field_name in ['name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())
        super(Game, self).save(*args, **kwargs)
