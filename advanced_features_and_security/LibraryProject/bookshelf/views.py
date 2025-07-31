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


from .forms import ExampleForm

def form_example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Securely process form data
            cleaned_data = form.cleaned_data
            # ... logic
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
