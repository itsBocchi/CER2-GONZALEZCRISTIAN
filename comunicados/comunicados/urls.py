from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_comunicado/', views.crear_comunicado, name='crear_comunicado'),
    path('core/', views.lista_comunicados, name='lista_comunicados'),
    path('core/filtrar/<str:nivel>/', views.filtrar_comunicados, name='filtrar_comunicados'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('' , views.home, name='home'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('registro/', views.registro, name='registro'),

]
