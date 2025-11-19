from django.db import models

class Aula(models.Model):
    TIPOS_AULA = (
        ("video", "Vídeo"),
        ("texto", "Texto"),
        ("pdf", "PDF"),
    )

    STATUS_AULA = (
        ("ativa", "Ativa"),
        ("inativa", "Inativa"),
    )

    modulo = models.ForeignKey("Modulo", on_delete=models.CASCADE, related_name="aulas")
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    # Campos simples adicionados
    tipo = models.CharField(max_length=20, choices=TIPOS_AULA, default="video")
    duracao = models.DurationField(null=True, blank=True)  # HH:MM:SS
    status = models.CharField(max_length=20, choices=STATUS_AULA, default="ativa")
    ordem = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.modulo.titulo} - {self.titulo}"

