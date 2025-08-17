from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    """
    Handles GET (list all books) and POST (create new book).
    - GET is public (anyone can see)
    - POST requires authentication
    - Supports filtering by ?year=YYYY
    """
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        year = self.request.query_params.get("year")
        if year:
            queryset = queryset.filter(publication_year=year)
        return queryset

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, PATCH, DELETE for a single book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
