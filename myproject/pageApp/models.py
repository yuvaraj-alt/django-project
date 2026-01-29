from django.db import models

# Create your models here.
class PageModel(models.Model):
    playerName = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    playerArm = models.CharField(max_length=100)
    instaFollowers = models.IntegerField()

    def __str__(self):
        return self.playerName

