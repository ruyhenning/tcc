from django.db import models

# Create your models here.

# -------------------------
#  MÓDULO
# -------------------------
class Modulo(models.Model):
    # Usamos string "Curso" para evitar import circular
    
    titulo = models.CharField(max_length=200)
    ordem = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.curso.nome} - {self.titulo}"

