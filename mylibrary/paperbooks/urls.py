from . import views
from django.urls import  path, re_path

urlpatterns = [
    path('register', views.RegisterFormView.as_view(), name="register"),
    path('login', views.LoginFormView.as_view(), name="login"),
    path('logout', views.LogoutView.as_view(), name="logout"),
    path('password-change', views.PasswordChangeView.as_view(), name="password-change"),
    path('', views.home, name="home"),
    path('paperbooks/', views.index, name="warehous"),
    path('paperbooks/index', views.index, name="warehous"),
    path('index', views.index, name="index"),
    
]
