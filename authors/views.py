from rest_framework import generics
from books.models import Book
from .models import Authors
from .pagination import AuthorListPagination, AuthorBookPagination
from .serializers import AuthorSerializer, AuthorBookListSerializer


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorListPagination


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'


class AuthorBooksListView(generics.ListAPIView):
    serializer_class = AuthorBookListSerializer
    pagination_class = AuthorBookPagination

    def get_queryset(self):
        return Book.objects.filter(authors__id=self.kwargs['pk'])
