from django.urls import path
from . import views

urlpatterns = [
    path("modulos/", views.lista_modulos, name="lista_modulos"),
    path("modulos/<int:id>/", views.detalhe_modulo, name="detalhe_modulo"),
    path("modulos/criar/", views.criar_modulo, name="criar_modulo"),
    path("modulos/<int:id>/editar/", views.editar_modulo, name="editar_modulo"),
    path("modulos/<int:id>/excluir/", views.excluir_modulo, name="excluir_modulo"),
]
