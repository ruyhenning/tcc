from django.shortcuts import render, redirect

# 1. Lista (Já tínhamos feito esta)
def lista_aulas(request):
    contexto = {'titulo': 'Gestão de Aulas'}
    return render(request, 'aulas/lista_aulas.html', contexto)

# 2. Detalhe (A que estava a dar erro agora)
def detalhe_aula(request, id):
    # No futuro, buscaremos a aula pelo ID aqui
    return render(request, 'aulas/detalhe_aula.html', {'id': id})

# 3. Criar
def criar_aula(request):
    return render(request, 'aulas/form_aula.html')

# 4. Editar
def editar_aula(request, id):
    return render(request, 'aulas/form_aula.html', {'id': id})

# 5. Excluir
def excluir_aula(request, id):
    # Por enquanto, apenas redireciona para a lista
    return redirect('lista_aulas')

# Adiciona isto no final do ficheiro aulas/views.py

def aulas_do_modulo(request, modulo_id):
    # Aqui iríamos buscar as aulas filtradas pelo id do módulo
    # Por agora, mostramos apenas uma mensagem a dizer que funcionou
    contexto = {
        'titulo': f'Aulas do Módulo {modulo_id}',
        'modulo_id': modulo_id
    }
    # Podemos reutilizar o template da lista de aulas
    return render(request, 'aulas/lista_aulas.html', contexto)