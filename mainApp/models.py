from django.db import models
from django.contrib.auth.models import User


class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    yosh = models.PositiveIntegerField()
    kasbi = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=255)
    sana = models.DateField()
    mavzu = models.CharField(max_length=255)
    matn = models.TextField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
