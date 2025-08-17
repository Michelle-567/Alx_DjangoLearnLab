from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


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


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend

# List all books
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"

from rest_framework import generics, filters
from django_filters import rest_framework as django_filters
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable Filtering, Searching, Ordering
    filter_backends = [
        django_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Define available filters
    filterset_fields = ['title', 'author', 'publication_year']

    # Define searchable fields
    search_fields = ['title', 'author']

    # Define ordering fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# Retrieve details of a single book
class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"
    permission_classes = [IsAuthenticatedOrReadOnly]



# Create a new book
class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author", "publication_year"]
    template_name = "book_form.html"
    success_url = reverse_lazy("book-list")
    permission_classes = [IsAuthenticated]



# Update an existing book
class BookUpdateView(UpdateView):
    model = Book
    fields = ["title", "author", "publication_year"]
    template_name = "book_form.html"
    success_url = reverse_lazy("book-list")
    permission_classes = [IsAuthenticated]



# Delete a book
class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_confirm_delete.html"
    success_url = reverse_lazy("book-list")
    permission_classes = [IsAuthenticated]

