from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'), # index 페이지
    path('create/', views.create, name='create'), # 신규 article 생성
]
