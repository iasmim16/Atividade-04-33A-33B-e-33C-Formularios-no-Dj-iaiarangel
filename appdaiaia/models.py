from django.db import models

class Beneficios(models.Model):
  INTENSIDADE = [
    ("P", "Pouca"),
    ("M", "Media"),
    ("I", "Intensa"),
  ]
  categoria = models.CharField(max_length=50)
  intensidade = models.CharField(max_length=1, choices=INTENSIDADE)
  melhoria = models.CharField(max_length=50)
  como_fazer = models.CharField(max_length=50)

class Principios(models.Model):
  tipo = models.CharField(max_length=50)
  prioridade = models.CharField(max_length=50)
  data_criacao = models.DateField()
  criador = models.CharField(max_length=50)
  