
from django.urls import path
from . import views

urlpatterns = [
    path('', views.opçoes_cursos, name='opçoes_cursos'),#seria/tarefa/
    path('<int:cursos_id>/', views.detalhe_cursos, name='detalhe_cursos'),

    #adicionar tarefas
    path('adicionar/', views.adicionar_cursos,name = 'adicionar_cursos'),

    #adicionar tarefa
    path('<int:atividade_id>/alterar/', views.alterar_atividade, name='alterar_atividade'),

#excluir tarefa
path('<int:atividade_id>/excluir/', views.excluir_atividade, name='excluir_atividade')
    ]
