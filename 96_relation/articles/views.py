<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
=======
from django.shortcuts import get_object_or_404, render, redirect
from .models import Article, Comment
from .forms import CommentForm

# Create your views here.

>>>>>>> fdb1a7bf510986878a22a39d23404433d2e59c6d
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
<<<<<<< HEAD
    
    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()

    context = {
        'article_form': article_form,
    }

    return render(request, 'articles/create.html', context)
    

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
=======

    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()

>>>>>>> fdb1a7bf510986878a22a39d23404433d2e59c6d
    context = {
        'article': article,
        'comment_form': comment_form,
    }

    return render(request, 'articles/detail.html', context)

<<<<<<< HEAD
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)

    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article_id = pk
        comment.user = request.user
        comment.save()
    
    return redirect('articles:detail', pk)
=======

def comments_create(request, pk):
    # article 인스턴스를 사용하는 방법
    # article = Article.objects.get(pk=pk)

    # comment_form = CommentForm(request.POST)
    # if comment_form.is_valid():
    #     comment = comment_form.save(commit=False)
    #     comment.article = article
    #     comment.save()
    
    # return redirect('articles:detail', pk)

    # article_id를 이용하는 방법
    article = Article.objects.get(pk=pk)

    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article_id = pk
        comment.save()
    
    return redirect('articles:detail', pk)

>>>>>>> fdb1a7bf510986878a22a39d23404433d2e59c6d
