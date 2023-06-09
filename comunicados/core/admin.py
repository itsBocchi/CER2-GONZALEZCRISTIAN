from django.contrib import admin
from .models import Categoria, Comunicado

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nivel', 'categoria', 'fecha_envio', 'fecha_modificacion', 'usuario')
    list_filter = ('nivel', 'categoria', 'fecha_envio', 'fecha_modificacion')
    search_fields = ('titulo', 'usuario__username')

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        super().save_model(request, obj, form, change)