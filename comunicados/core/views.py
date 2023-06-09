from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Comunicado, Categoria
from .forms import UsuarioForm, ComunicadoForm, CategoriaForm
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'core/home.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la página de login
            return redirect('login')
    return render(request, 'registro.html')

@login_required
def crear_usuario(request):
    # Verificar si el usuario actual es superadmin
    if not request.user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UsuarioForm()
    render(request, 'core/crear_usuario.html')

@login_required
def crear_comunicado(request):
    if request.method == 'POST':
        form = ComunicadoForm(request.POST)
        if form.is_valid():
            comunicado = form.save(commit=False)
            comunicado.usuario = request.user
            comunicado.save()
            return redirect('home')
    else:
        form = ComunicadoForm()
    
    return render(request, 'core/crear_comunicado.html', {'form': form})

def lista_comunicados(request):
    comunicados = Comunicado.objects.all()
    return render(request, 'core/lista_comunicados.html', {'comunicados': comunicados})

def filtrar_comunicados(request, nivel):
    comunicados = Comunicado.objects.filter(nivel=nivel)
    return render(request, 'core/lista_comunicados.html', {'comunicados': comunicados})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    
    return render(request, 'core/crear_categoria.html', {'form': form})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/lista_categorias.html', {'categorias': categorias})
