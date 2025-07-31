from django.shortcuts import render

# # Create your views here.
# from django.contrib.auth.decorators import permission_required
# from django.shortcuts import render
# from .models import Article

# @permission_required('yourapp.can_view', raise_exception=True)
# def view_articles(request):
#     articles = Article.objects.all()
#     return render(request, 'articles.html', {'articles': articles})

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
