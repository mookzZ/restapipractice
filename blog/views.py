from rest_framework import generics, permissions

from .models import Category, Publication
from .serializers import CategorySerializer, PublishSerializer
from .permissions import IsCreatorOrReadOnly

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PublicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publication.objects.filter(is_archived=False)
    serializer_class = PublishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PublicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.filter(is_archived=False)
    serializer_class = PublishSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]