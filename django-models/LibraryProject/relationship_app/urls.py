from django.urls import path
from .views import LibraryDetailView, list_books

urlpatterns = [
    path('books/', list_books, name='list-books'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # class-based view
]

from django.urls import path
from . import views

# urlpatterns = [
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     # Add your other views as needed
# ]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Existing views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    
    # Other views...
    path('', views.list_books, name='list_books'),  # Replace with your actual 
    
    path('member/', views.member_view, name='member_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('admin/', views.admin_view, name='admin_view'),

    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]

