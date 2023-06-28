from . import views
from django.urls import  path


urlpatterns = [
    path('register', views.RegisterFormView.as_view(), name="register"),
    path('login', views.LoginFormView.as_view(), name="login"),
    path('logout', views.LogoutView.as_view(), name="logout"),
    path('password-change', views.PasswordChangeView.as_view(), name="password-change"),
    path('', views.index, name="home"),
    path('party/', views.home, name="index"),
    path('party/index', views.index, name="index"),
    path('party/new_event', views.new_event, name="create-event"),
    path('party/list_events', views.list_events, name="list-events"),
    path('party/portfolio', views.portfolio, name="portfolio"),
    path('party/staff', views.staff, name="staff"),
]
