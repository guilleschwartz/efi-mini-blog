import pytest
from miniblog.models import Post, Categoria

@pytest.mark.django_db
def test_new_post():
    Post.objects.create(titulo='test', contenido='test')
    assert Post.objects.count() == 1

@pytest.mark.django_db
def test_new_categoria():
    Categoria.objects.create(nombre='test')
    assert Categoria.objects.count() == 1
