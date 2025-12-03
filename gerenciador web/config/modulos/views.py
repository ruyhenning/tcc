from django.shortcuts import render, redirect

# Se tiveres o modelo Modulo, descomenta a linha abaixo:
# from .models import Modulo

# 1. Listar Módulos (Já existia)
def lista_modulos(request):
    contexto = {'titulo': 'Gestão de Módulos'}
    return render(request, 'modulos/lista_modulos.html', contexto)

# 2. Detalhe do Módulo (O erro atual)
def detalhe_modulo(request, id):
    # Futuramente buscamos o módulo pelo ID
    contexto = {'id': id, 'titulo': f'Detalhe do Módulo {id}'}
    return render(request, 'modulos/detalhe_modulo.html', contexto)

# 3. Criar Módulo
def criar_modulo(request):
    return render(request, 'modulos/form_modulo.html')

# 4. Editar Módulo
def editar_modulo(request, id):
    contexto = {'id': id}
    return render(request, 'modulos/form_modulo.html', contexto)

# 5. Excluir Módulo
def excluir_modulo(request, id):
    # Por agora, apenas redireciona para a lista
    return redirect('lista_modulos')