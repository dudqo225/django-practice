from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article
from .forms import ArticleForm

# Create your views here.

# READ - 목록 페이지
@require_safe
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)


# READ - 상세 페이지
@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


# CREATE -  신규 article 생성 페이지
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    
    context = {
        'form': form,
    }

    return render(request, 'articles/form.html', context)


# UPDATE - 기존 article 수정 페이지
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'form': form,
    }
    
    return render(request, 'articles/form.html', context)


# DELETE - article 삭제
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()

    return redirect('articles:index')