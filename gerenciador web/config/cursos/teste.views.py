import pytest
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from cursos.models import Curso


# ---------------------------------------------------------
# LISTAR CURSOS
# ---------------------------------------------------------
@pytest.mark.django_db
def test_lista_cursos(client):
    Curso.objects.create(nome="Curso 1", carga_horaria=10)
    Curso.objects.create(nome="Curso 2", carga_horaria=20)

    url = reverse("lista_cursos")
    resposta = client.get(url)

    assert resposta.status_code == 200
    assert "meus_cursos" in resposta.context
    assert len(resposta.context["meus_cursos"]) == 2
    assert "cursos/lista.html" in [t.name for t in resposta.templates]


# ---------------------------------------------------------
# DETALHE DO CURSO
# ---------------------------------------------------------
@pytest.mark.django_db
def test_detalhe_curso(client):
    curso = Curso.objects.create(nome="Curso Teste", carga_horaria=10)

    url = reverse("detalhe_curso", args=[curso.id])
    resposta = client.get(url)

    assert resposta.status_code == 200
    assert resposta.context["curso"] == curso
    assert "cursos/detalhe.html" in [t.name for t in resposta.templates]


# ---------------------------------------------------------
# CRIAR CURSO - GET
# ---------------------------------------------------------
@pytest.mark.django_db
def test_criar_curso_get(client):
    url = reverse("criar_curso")
    resposta = client.get(url)

    assert resposta.status_code == 200
    assert "form" in resposta.context
    assert "cursos/form_curso.html" in [t.name for t in resposta.templates]


# ---------------------------------------------------------
# CRIAR CURSO - POST
# ---------------------------------------------------------
@pytest.mark.django_db
def test_criar_curso_post(client):
    url = reverse("criar_curso")

    fake_image = SimpleUploadedFile(
        "capa.jpg", b"conteudo", content_type="image/jpeg"
    )

    dados = {
        "nome": "Curso Novo",
        "descricao": "descrição teste",
        "nivel": "basico",
        "carga_horaria": 10,
        "ativo": True,
    }

    resposta = client.post(url, dados, follow=True, FILES={"capa": fake_image})

    assert resposta.status_code == 200
    assert Curso.objects.count() == 1
    assert Curso.objects.first().nome == "Curso Novo"


# ---------------------------------------------------------
# EDITAR CURSO - GET
# ---------------------------------------------------------
@pytest.mark.django_db
def test_editar_curso_get(client):
    curso = Curso.objects.create(nome="Curso Original", carga_horaria=5)

    url = reverse("editar_curso", args=[curso.id])
    resposta = client.get(url)

    assert resposta.status_code == 200
    assert resposta.context["form"] is not None
    assert "cursos/form_curso.html" in [t.name for t in resposta.templates]


# ---------------------------------------------------------
# EDITAR CURSO - POST
# ---------------------------------------------------------
@pytest.mark.django_db
def test_editar_curso_post(client):
    curso = Curso.objects.create(nome="Curso Antigo", carga_horaria=5)

    url = reverse("editar_curso", args=[curso.id])
    dados = {
        "nome": "Curso Editado",
        "descricao": "",
        "nivel": "basico",
        "carga_horaria": 8,
        "ativo": True,
    }

    resposta = client.post(url, dados, follow=True)

    curso.refresh_from_db()
    assert curso.nome == "Curso Editado"
    assert resposta.status_code == 200


# ---------------------------------------------------------
# EXCLUIR CURSO - GET
# ---------------------------------------------------------
@pytest.mark.django_db
def test_excluir_curso_get(client):
    curso = Curso.objects.create(nome="Curso Para Excluir")

    url = reverse("excluir_curso", args=[curso.id])
    resposta = client.get(url)

    assert resposta.status_code == 200
    assert "cursos/confirmar_exclusao.html" in [t.name for t in resposta.templates]


# ---------------------------------------------------------
# EXCLUIR CURSO - POST
# ---------------------------------------------------------
@pytest.mark.django_db
def test_excluir_curso_post(client):
    curso = Curso.objects.create(nome="Curso Para Excluir")

    url = reverse("excluir_curso", args=[curso.id])
    resposta = client.post(url, follow=True)

    assert resposta.status_code == 200
    assert Curso.objects.count() == 0
