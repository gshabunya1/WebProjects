from . import views
from django.urls import  path, re_path

urlpatterns = [
    path('register', views.RegisterFormView.as_view()),
    path('login', views.LoginFormView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('password-change', views.PasswordChangeView.as_view()),
    path('', views.home, name="home"),
    path('paperbooks/', views.index, name="warehous"),
    path('paperbooks/index/', views.index, name="index"),
    path('index/', views.index, name="index"),
    
]
