# from django.shortcuts import render, redirect
# from django.views.generic.detail import DetailView
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.views import LoginView, LogoutView
# from .models import Library, Book, UserProfile

# # Class-based view
# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'

# # Function-based view for listing all books
# def list_books(request):
#     books = Book.objects.all()
#     return render(request, 'relationship_app/list_books.html', {'books': books})

# # Register view
# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Automatically log the user in
#             return redirect('list_books')  # Redirect after successful registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})

# # ✅ Login view
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('list_books')  # Or another landing page
#     else:
#         form = AuthenticationForm()
#     return render(request, 'relationship_app/login.html', {'form': form})

# # ✅ Logout view
# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('login')  # Redirect to login after logout
#     return render(request, 'relationship_app/logout.html')

# # ✅ Role-based access
# def role_required(role):
#     def check_role(user):
#         return hasattr(user, 'userprofile') and user.userprofile.role == role
#     return user_passes_test(check_role)

# @login_required
# @role_required('Admin')
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# @login_required
# @role_required('Librarian')
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @login_required
# @role_required('Member')
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')


# from django.contrib.auth.decorators import user_passes_test
# from django.shortcuts import render

# def is_member(user):
#     return user.groups.filter(name='Member').exists()

# def is_librarian(user):
#     return user.groups.filter(name='Librarian').exists()

# def is_admin(user):
#     return user.groups.filter(name='Admin').exists()

# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from .models import Library, Book, UserProfile

# ✅ Class-based view for a specific Library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ✅ Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ✅ Register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# ✅ Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# ✅ Logout view
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'relationship_app/logout.html')

# ✅ Role checks using user_passes_test

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

from django.contrib.auth.decorators import login_required, user_passes_test

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
