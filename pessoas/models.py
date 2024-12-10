# pessoas/models.py
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_de_nascimento = models.DateField()

    def __str__(self):
        return self.nome
