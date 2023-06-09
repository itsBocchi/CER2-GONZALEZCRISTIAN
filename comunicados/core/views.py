from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Comunicado, Categoria
from .forms import CrearUsuarioForm, ComunicadoForm, CategoriaForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    nivel_filter = request.GET.get('nivel', '')  # Obtener el valor seleccionado del menú desplegable de nivel
    categoria_filter = request.GET.get('categoria', '')  # Obtener el valor seleccionado del menú desplegable de categoría

    comunicados = Comunicado.objects.order_by('-fecha_envio')

    if nivel_filter:
        comunicados = comunicados.filter(nivel=nivel_filter)

    if categoria_filter:
        comunicados = comunicados.filter(categoria=categoria_filter)

    return render(request, 'home.html', {'comunicados': comunicados})

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
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the name of the URL pattern for your homepage
    else:
        form = CrearUsuarioForm()
    
    return render(request, 'crear_usuario.html', {'form': form})


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
    # localhost:8000/comunicados/filtrar/GEN
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

def login_view(request):
    if request.method == 'POST':
        # Procesar los datos del formulario de login
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Reemplaza 'home' con el nombre de tu URL de la página de inicio

    return render(request, 'login.html')

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/lista_categorias.html', {'categorias': categorias})
