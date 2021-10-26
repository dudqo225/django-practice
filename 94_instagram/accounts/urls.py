from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'), # 회원가입
    path('login/', views.login, name='login'), # 로그인
    path('<username>/', views.profile, name='profile'), # 프로필 페이지
    path('<int:pk>/follow/', views.follow, name='follow'), # 팔로우
]
