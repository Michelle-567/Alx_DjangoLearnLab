from django.urls import path
from .views import LibraryDetailView, list_books

urlpatterns = [
    path('books/', list_books, name='list-books'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # class-based view
]

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Add your other views as needed
]
