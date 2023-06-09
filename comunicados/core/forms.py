from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comunicado, Categoria

class UsuarioForm(UserCreationForm):
    pass

class ComunicadoForm(forms.ModelForm):
    class Meta:
        model = Comunicado
        fields = ('titulo', 'detalle', 'nivel', 'categoria')

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre','detalles',)
