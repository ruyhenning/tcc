class Modulo(models.Model):
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE, related_name="modulos")

    titulo = models.CharField(max_length=200)
    ordem = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.curso.nome} - {self.titulo}"
