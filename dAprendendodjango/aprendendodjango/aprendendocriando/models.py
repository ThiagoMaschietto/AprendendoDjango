from django.db import models

# Create your models here.
class Imagen(models.Model):
    nome          = models.CharField(max_length=100)
    imagem_url    = models.URLField(max_length=200)
    descricao     = models.CharField(max_length=500000, null = True)
