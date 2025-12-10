from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Curso


class CursoModelTest(TestCase):

    def test_criacao_curso(self):
        curso = Curso.objects.create(
            nome='Curso Django',
            descricao='Curso completo',
            nivel='basico',
            carga_horaria=20
        )
        self.assertIsNotNone(curso.id)
        self.assertEqual(curso.nome, 'Curso Django')
        self.assertTrue(curso.ativo)

    def test_default_nivel(self):
        curso = Curso.objects.create(nome='Outro Curso')
        self.assertEqual(curso.nivel, 'basico')

    def test_str_representation(self):
        curso = Curso.objects.create(nome='Teste')
        self.assertEqual(str(curso), 'Teste')

    def test_upload_capa(self):
        image = SimpleUploadedFile(
            'teste.jpg', b'conteudo', content_type='image/jpeg'
        )
        curso = Curso.objects.create(nome='Com Capa', capa=image)
        self.assertTrue(curso.capa.name.startswith('cursos/capas/'))
