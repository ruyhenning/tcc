from django.urls import path
from . import views

urlpatterns = [
    # --- AULAS ---
    path("aulas/", views.lista_aulas, name="lista_aulas"),
    path("aulas/<int:id>/", views.detalhe_aula, name="detalhe_aula"),
    path("aulas/criar/", views.criar_aula, name="criar_aula"),
    path("aulas/<int:id>/editar/", views.editar_aula, name="editar_aula"),
    path("aulas/<int:id>/excluir/", views.excluir_aula, name="excluir_aula"),

    # Aulas dentro do módulo
    path("modulos/<int:modulo_id>/aulas/", views.aulas_do_modulo, name="aulas_do_modulo"),
]
