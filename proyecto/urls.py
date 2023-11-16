from django.contrib import admin
from django.urls import path, include
from miniblog.api.api_views import CategoriaViewSet, PostViewSet
from rest_framework.routers import DefaultRouter
from miniblog import views

# Rutas de API
router = DefaultRouter()
router.register(r'api/categorias', CategoriaViewSet)
router.register(r'api/posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('post/<int:id>', views.post, name='post'),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('editar_post/<int:id>', views.editar_post, name='editar_post'),
    path('eliminar_post/<int:id>', views.eliminar_post, name='eliminar_post'),
    path('lista_post/', views.lista_post, name='lista_post'),
    path('categoria/<int:id>', views.categoria, name='categoria'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('editar_categoria/<int:id>', views.editar_categoria, name='editar_categoria'),
    path('eliminar_categoria/<int:id>', views.eliminar_categoria, name='eliminar_categoria'),
    path('usuario/<int:id>', views.usuario, name='usuario'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('editar_usuario/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('eliminar_usuario/<int:id>', views.eliminar_usuario, name='eliminar_usuario'),
    # Api
    path('', include(router.urls)),
]
