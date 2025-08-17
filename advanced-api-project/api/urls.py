from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDeleteView
from django.urls import path
from .views import BookListView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookRetrieveUpdateDeleteView.as_view(), name="book-detail"),
    

    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]


