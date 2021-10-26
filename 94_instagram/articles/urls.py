from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'), # 인덱스 페이지
    path('create/', views.create, name='create'), # 신규 article 생성
    path('<int:pk>/comments/create/', views.comments_create, name='comments_create'), # 코멘트 생성
    path('<int:pk>/likes/', views.likes, name='likes'), # 좋아요
]
