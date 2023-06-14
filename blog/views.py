from django.shortcuts import render
from .models import Article
# Create your views here.

def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'liste_articles.html', {'articles': articles})
