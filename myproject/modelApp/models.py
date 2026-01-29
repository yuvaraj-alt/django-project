from django.db import models

# Create your models here.
class Players(models.Model):
    playerName = models.CharField(max_length=100)
    teamName = models.CharField(max_length=100)
    whichCountry = models.CharField(max_length=100)
    PlayedMatches = models.IntegerField()
    centuries = models.IntegerField()

    def __str__(self):
        return self.playerName





