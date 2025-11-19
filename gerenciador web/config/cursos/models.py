from django.db import models

from django.db import models


class Curso(models.Model):
    NIVEL = (
        ("basico", "Básico"),
        ("intermediario", "Intermediário"),
        ("avancado", "Avançado"),
    )

    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    capa = models.ImageField(upload_to="cursos/capas/", blank=True, null=True)
    nivel = models.CharField(max_length=20, choices=NIVEL, default="basico")

    carga_horaria = models.PositiveIntegerField(default=0)  # em horas
    criado_em = models.DateTimeField(auto_now_add=True)

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

