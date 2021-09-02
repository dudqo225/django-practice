from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 전체 article 보여주기
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

# 신규 article 생성
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 1. 사용자 데이터 가져오기
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. DB에 저장하기
    Article.objects.create(title=title, content=content)

    return redirect('articles:index')

# 개별 article 페이지 보여주기
def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)

# article 수정하기
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)

# article 삭제하기
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')