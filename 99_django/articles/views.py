from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 1. 사용자가 입력한 데이터 받아오기
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. 가져온 데이터 저장하기
    article = Article(title=title, content=content)
    article.save()

    # 3. index페이지로 리다이렉트 처리
    return redirect('articles:index')

def delete(request, pk):
    # 1. 지울 article 찾기
    article = Article.objects.get(pk=pk)
    
    # 2. 찾은 article 지우기
    article.delete()

    # 3. index페이지로 리다이렉트 처리
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 1. 기존 정보
    article = Article.objects.get(pk=pk)

    # 2. 새로운 정보
    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)