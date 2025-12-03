from django.db import models

class Aula(models.Model):
   
    modulo = models.ForeignKey('modulos.Modulo', related_name='aulas', on_delete=models.CASCADE)
    
    nome = models.CharField(max_length=200)
    video_url = models.URLField(max_length=200, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome