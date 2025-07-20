from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

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
    path('', views.book_list, name='book_list'),  # Home page or book list
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
