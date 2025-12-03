from django.urls import path
from . import views

urlpatterns = [
    # Mudamos de "cursos/" para "" (vazio).
    # Assim, o endereço fica apenas /cursos/ em vez de /cursos/cursos/
    path("", views.lista_cursos, name="lista_cursos"),
    
    path("<int:id>/", views.detalhe_curso, name="detalhe_curso"),
    path("criar/", views.criar_curso, name="criar_curso"),
    path("<int:id>/editar/", views.editar_curso, name="editar_curso"),
    path("<int:id>/excluir/", views.excluir_curso, name="excluir_curso"),
]