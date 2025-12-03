from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm

# NOME CORRIGIDO: de 'listar_cursos' para 'lista_cursos'
def lista_cursos(request):
    cursos_salvos = Curso.objects.all()
    contexto = {
        'meus_cursos': cursos_salvos
    }
    return render(request, 'cursos/lista.html', contexto)

def detalhe_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    contexto = {'curso': curso}
    return render(request, 'cursos/detalhe.html', contexto)

def criar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/form_curso.html', {'form': form})

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == "POST":
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/form_curso.html', {'form': form})

def excluir_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == "POST":
        curso.delete()
        return redirect('lista_cursos')
    return render(request, 'cursos/confirmar_exclusao.html', {'curso': curso})