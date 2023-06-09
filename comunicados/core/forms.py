from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comunicado, Categoria
from django.contrib.auth.models import User

class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ComunicadoForm(forms.ModelForm):
    class Meta:
        model = Comunicado
        fields = ('titulo', 'detalle', 'nivel', 'categoria')

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre','detalles',)
