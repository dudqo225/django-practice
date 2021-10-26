from django.shortcuts import render, redirect
from .forms import ArticleForm

# Create your views here.

# index 페이지
def index(request):
    return render(request, 'articles/index.html')

# 신규 article 생성
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/form.html', context)