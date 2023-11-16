import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from miniblog.models import Categoria, Post

@pytest.mark.django_db
def test_api_endpoints():
    client = APIClient()

    # Crear una categoría
    response = client.post('/api/categorias/', {'nombre': 'TestCategory'}, format='json')
    assert response.status_code == 201

    # Obtener la lista de categorías
    response = client.get('/api/categorias/')
    assert response.status_code == 200
    assert len(response.data) == 1

    # Crear un post asociado a la categoría creada
    categoria_id = response.data[0]['id']
    response = client.post('/api/posts/', {'titulo': 'TestPost', 'contenido': 'Contenido de prueba', 'categorias': [categoria_id]}, format='json')
    assert response.status_code == 201

    # Obtener la lista de posts
    response = client.get('/api/posts/')
    assert response.status_code == 200
    assert len(response.data) == 1
