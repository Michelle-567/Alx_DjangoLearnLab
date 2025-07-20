# from django.urls import path
# from .views import list_books, LibraryDetailView

# urlpatterns = [
#     path('books/', list_books, name='list_books'),  # function-based view
#     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # class-based view
    
# ]
from django.urls import path
from .views import LibraryDetailView, list_books

urlpatterns = [
    path('books/', list_books, name='list-books'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # class-based view
]
