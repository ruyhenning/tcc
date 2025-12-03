from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        # Incluímos todos os campos que queremos no formulário
        fields = ['nome', 'descricao', 'capa', 'nivel', 'carga_horaria', 'ativo']