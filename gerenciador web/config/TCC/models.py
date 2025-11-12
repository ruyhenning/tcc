from django.db import models
from cursos.models import Cursos


class Ead (models.Model):

    proficiências = models.CharField(max_length = 200)

    descricao = models.TextField(blank=True, null=True)

    data_inicio = models.DateTimeField (auto_now_add = True)

    concluida = models.BooleanField(default = False)
    Cursos = models.ForeignKey(Cursos, on_delete =models.CASCADE, null = True, blank = True)

    #exibir titulo por padrão
    def __str__(self):
        return self.Cursos
