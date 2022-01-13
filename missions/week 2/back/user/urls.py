from django.urls import path,re_path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),

    # 카카오톡
    # path('kakaoLoginLogic/', views.kakaoLoginLogic),
    # path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect),
    # path('kakaoLogout/', views.kakaoLogout),

    # 소셜로그인 관련 url
    # re_path(r'^accounts/', include('accountapp.urls')),
    # re_path(r'^accounts/', include('allauth.urls')),
    # path('accounts/kakao/login/', views.kakao_login, name='kakao_login'),
    # path('accounts/kakao/callback/', views.kakao_callback, name='kakao_callback'),
    # path('accounts/kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),

    # 아이디 찾기
    path('forgot_id/',views.ForgotIDView, name="forgot_id"),

    # 비밀번호 초기화
    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
