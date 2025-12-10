from django.test import TestCase
from .models import Modulo, Curso


class ModuloModelTest(TestCase):

    def setUp(self):
        # Criamos um curso para associar ao módulo
        self.curso = Curso.objects.create(
            nome="Curso de Python",
            descricao="Descrição teste",
            nivel="basico",
            carga_horaria=40
        )

    def test_criacao_modulo(self):
        modulo = Modulo.objects.create(
            curso=self.curso,
            titulo="Módulo 1",
            ordem=1
        )

        self.assertEqual(modulo.titulo, "Módulo 1")
        self.assertEqual(modulo.ordem, 1)
        self.assertEqual(modulo.curso, self.curso)

    def test_valor_padrao_ordem(self):
        modulo = Modulo.objects.create(
            curso=self.curso,
            titulo="Módulo Padrão"
        )
        self.assertEqual(modulo.ordem, 1)  # default

    def test_str_representation(self):
        modulo = Modulo.objects.create(
            curso=self.curso,
            titulo="Módulo X"
        )

        expected_str = f"{self.curso.nome} - Módulo X"
        self.assertEqual(str(modulo), expected_str)
