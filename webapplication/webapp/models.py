from django.db import models


# Create your models here.
class movie(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=250)
    disc = models.TextField()
    year = models.IntegerField()
    rateing = models.IntegerField()

    def __str__(self):
        return self.name
