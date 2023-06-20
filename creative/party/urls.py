from . import views
from django.urls import  path


urlpatterns = [
    path('register', views.RegisterFormView.as_view(), name="register"),
    path('login', views.LoginFormView.as_view(), name="login"),
    path('logout', views.LogoutView.as_view(), name="logout"),
    path('password-change', views.PasswordChangeView.as_view(), name="password-change"),
    path('', views.home, name="home"),
    path('party/', views.home, name="home"),
    path('party/index', views.index, name="index"),
]
