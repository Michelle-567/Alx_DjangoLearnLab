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


from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# DRF Views

# List all books / create new one
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Django Class-Based Views (to satisfy the "ListView", "DetailView", etc. requirement)

class BookListPageView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"


class BookDetailPageView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"


class BookCreatePageView(CreateView):
    model = Book
    fields = ["title", "author", "publication_year"]
    template_name = "book_form.html"
    success_url = "/books/"


class BookUpdatePageView(UpdateView):
    model = Book
    fields = ["title", "author", "publication_year"]
    template_name = "book_form.html"
    success_url = "/books/"


class BookDeletePageView(DeleteView):
    model = Book
    template_name = "book_confirm_delete.html"
    success_url = "/books/"
