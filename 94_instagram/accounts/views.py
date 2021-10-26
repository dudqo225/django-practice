from django.shortcuts import redirect, render, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user, login as auth_login
from django.contrib.auth import get_user_model
# Create your views here.

# 회원가입
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)

# 로그인
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('accounts:profile', user.username)

    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    
    return render(request, 'accounts/form.html', context)

# 프로필
def profile(request, username):
    User = get_user_model()

    profile_user = get_object_or_404(User, username=username)

    context = {
        'profile_user': profile_user,
    }

    return render(request, 'accounts/profile.html', context)

# 팔로우
def follow(request, pk):
    User = get_user_model()
    
    me = request.user
    you = get_object_or_404(User, pk=pk)

    if me in you.followers.all():
        # you.followers.remove(me)
        me.followings.remove(you)
    else:
        # you.followers.add(me)
        me.followings.add(you)

    return redirect('accounts:profile', you.username)