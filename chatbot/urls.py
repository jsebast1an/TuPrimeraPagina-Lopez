from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path('profile/', views.profile_view, name='profile'),
    path('chat/', views.chat_view, name='chat'),
    path('users/', views.users_view, name='users'),
    path('about/', views.about_view, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]