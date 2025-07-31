from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books, LibraryDetailView


# urlpatterns = [
#     # Auth views
#     path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
#     path('register/', views.register_view, name='register'),

#     # Role-specific views
#     path('member/', views.member_view, name='member_view'),
#     path('librarian/', views.librarian_view, name='librarian_view'),
#     path('admin/', views.admin_view, name='admin_view'),

#     # Book-related views
#     path('', views.book_list, name='book_list'),  # Home page or book list
#     path('add_book/', views.add_book, name='add_book'),
#     path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
#     path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
# ]
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books, LibraryDetailView  # ✅ Required for the check

urlpatterns = [
    # Auth views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),

    # Role-specific views
    path('member/', views.member_view, name='member_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('admin/', views.admin_view, name='admin_view'),

    # Book-related views
    path('', list_books, name='list_books'),  # ✅ Function-based view
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    # Library detail view (class-based view)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # ✅ Class-based view
]
