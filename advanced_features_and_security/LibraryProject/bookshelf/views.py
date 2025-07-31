from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Article

@permission_required('yourapp.can_view', raise_exception=True)
def view_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})
