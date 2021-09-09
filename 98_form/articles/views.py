from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .forms import ArticleForm
from .models import Article

# Create your views here.

# READ
@require_safe
def index(request):
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

@require_safe
def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


# CREATE
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        
    else: # GET 방식
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/form.html', context)


# UPDATE 
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    # 0. 기존 정보 가져오기
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)

    # 5. update 요청이 POST 방식으로 들어옴 > 잘못된 데이터를 담아서 수정해달라고 요청
    # 10. update 요청이 POST 방식으로 들어옴 > 올바른 데이터를 담아서 수정해달라고 요청
    if request.method == 'POST':
        # 6. ArticleForm을 인스턴스화 한다. (사용자가 수정한 정보 + 기존정보)
        # 11. ArticleForm을 인스턴스화 한다. (사용자가 수정한 정보 + 기존정보)
        form = ArticleForm(request.POST, instance=article)
        # 7. 데이터가 유효한지 검증을 한다. (잘못된 정보가 들어옴)
        # 12. 데이터가 유효한지 검증을 한다. (올바른 정보가 들어옴)
        if form.is_valid():
            # 13. 데이터를 수정한다.
            form.save()
            # 14. index로 리다이렉트 시켜준다.
            return redirect('articles:index')
    
    # 1. update 요청이 GET 방식으로 들어옴 > 기존의 정보를 담은 종이를 요청
    else:
        # 2. 기존의 정보를 담은 종이 생성
        form = ArticleForm(instance=article)
    
    # 3. 사용자에게 보여주기 위해 context에 저장
    # 8. 유효한 데이터만 들어있는 종이를 다시 돌려주기 위해 context에 저장
    context = {
        'form': form,
    }

    # 4. 사용자에게 종이를 보여준다.
    # 9. 사용자에게 올바른 데이터가 있는 종이를 넘겨준다.
    return render(request, 'articles/form.html', context)


# DELETE
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()

    return redirect('articles:index')