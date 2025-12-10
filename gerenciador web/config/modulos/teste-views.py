from django.test import TestCase
from django.urls import reverse


class CasosDeBordaModuloViewsTest(TestCase):

    def test_excluir_modulo_redireciona_para_lista(self):
        # como o módulo não existe no banco, testamos apenas a lógica da view
        url = reverse('excluir_modulo', args=[99])  # ID fictício

        response = self.client.post(url)

        self.assertRedirects(response, reverse('lista_modulos'))

    def test_lista_modulos_renderiza_template_correto(self):
        url = reverse('lista_modulos')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("titulo", response.context)
        self.assertEqual(response.context["titulo"], "Gestão de Módulos")
        self.assertTemplateUsed(response, 'modulos/lista_modulos.html')

    def test_detalhe_modulo_recebe_id_no_contexto(self):
        url = reverse('detalhe_modulo', args=[7])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.context)
        self.assertEqual(response.context["id"], 7)
        self.assertTemplateUsed(response, 'modulos/detalhe_modulo.html')

    def test_criar_modulo_retorna_template(self):
        url = reverse('criar_modulo')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'modulos/form_modulo.html')

    def test_editar_modulo_contexto_com_id(self):
        url = reverse('editar_modulo', args=[12])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.context)
        self.assertEqual(response.context["id"], 12)
        self.assertTemplateUsed(response, 'modulos/form_modulo.html')
