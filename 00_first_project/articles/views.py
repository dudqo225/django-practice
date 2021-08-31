from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['라면', '짜장면', '고기']
    info = {
        'name': '손영배',
        'location': '수원',
    }

    context = {
        'foods': foods,
        'info': info,
    }

    return render(request, 'articles/greeting.html', context)

def dinner(request):

    foods = ['삼겹살', '햄버거', '피자']
    pick = random.choice(foods)
    
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'articles/dinner.html', context)

# 사용자의 정보를 받아오기 위해 종이를 보여주는 함수
def throw(request):
    return render(request, 'articles/throw.html')

# 사용자가 입력한 정보를 받아와서 처리(CRUD)하는 함수
def catch(request):
    message = request.GET.get('message')

    context = {
        'message': message,
    }

    return render(request, 'articles/catch.html', context)


def fake_google(request):
    return render(request, 'articles/fake_google.html')


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)