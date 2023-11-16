from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post, Categoria
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'miniblog/home.html')


def usuario(request, id):
    usuario = User.objects.get(id=id)
    return render(request, 'miniblog/usuario/usuario.html', {'usuario': usuario})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        contraseña = request.POST.get('contraseña')
        User.objects.create_user(username=nombre_usuario, password=contraseña)
        return redirect('lista_usuarios')
    else:
        return render(request, 'miniblog/usuario/crear_usuario.html')


def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'miniblog/usuario/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def editar_usuario(request, id):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        contraseña = request.POST.get('contraseña')
        User.objects.filter(id=id).update(username=nombre_usuario, password=contraseña)
        return redirect('lista_usuarios')
    else:
        usuario = User.objects.get(id=id)
        return render(request, 'miniblog/usuario/editar_usuario.html', {'usuario': usuario})

@login_required
def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('lista_usuarios')


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'miniblog/posteos/post.html', {'post':post})


def categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, 'miniblog/categoria/categoria.html', {'categoria':categoria, 'posts':posts})


def lista_post(request):
    posts = Post.objects.all()
    return render(request, 'miniblog/posteos/lista_post.html', {'posts':posts})

@login_required
def crear_post(request):
    if request.POST:
        post = Post()
        post.titulo = request.POST['titulo']
        post.contenido = request.POST['contenido']
        post.save()
        return redirect('lista_post')
    else:
        return render(request, 'miniblog/posteos/crear_post.html')

@login_required
def editar_post(request, id):
    post = Post.objects.get(id=id)
    if request.POST:
        post.titulo = request.POST['titulo']
        post.contenido = request.POST['contenido']
        post.save()
        return redirect('lista_post')
    else:
        return render(request, 'miniblog/posteos/editar_post.html', {'post':post})

@login_required
def eliminar_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('lista_post')

@login_required
def crear_categoria(request):
    if request.POST:
        categoria = Categoria()
        categoria.nombre = request.POST['nombre']
        categoria.save()
        return redirect('home')
    else:
        return render(request, 'miniblog/categoria/crear_categoria.html')

@login_required
def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.POST:
        categoria.nombre = request.POST['nombre']
        categoria.save()
        return redirect('home')
    else:
        return render(request, 'miniblog/categoria/editar_categoria.html', {'categoria':categoria})

@login_required
def eliminar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('home')
