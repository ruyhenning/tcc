from django.urls import path
from . import views

urlpatterns = [
    path("cursos/", views.lista_cursos, name="lista_cursos"),
    path("cursos/<int:id>/", views.detalhe_curso, name="detalhe_curso"),
    path("cursos/criar/", views.criar_curso, name="criar_curso"),
    path("cursos/<int:id>/editar/", views.editar_curso, name="editar_curso"),
    path("cursos/<int:id>/excluir/", views.excluir_curso, name="excluir_curso"),
]
