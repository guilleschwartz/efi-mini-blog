# api/api_views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Post, Categoria
from ..serializers import PostSerializer, CategoriaSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]
