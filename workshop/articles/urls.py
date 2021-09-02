from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 전체 articles 보여주는 페이지 경로
    path('', views.index, name='index'),

    # 신규 article 작성
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # 개별 article 보여주는 페이지
    path('<int:pk>', views.detail, name='detail'),

    # article 수정하기 위해 기존 정보를 보여주는 페이지
    path('<int:pk>/edit/', views.edit, name='edit'),
    # 수정할 데이터를 받아와서 기존정보를 수정하는 로직
    path('<int:pk>/update/', views.update, name='update'),

    # 하나의 article을 삭제하는 경로
    path('<int:pk>/delete', views.delete, name='delete'),
]
