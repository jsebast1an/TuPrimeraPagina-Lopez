from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('chat/', views.chat_view, name='chat'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/edit/', views.UserUpdateView.as_view(), name='user-edit'),
    path('users/create/', views.UserCreateView.as_view(), name='user-create'),
    path('users/{<int:pk>}/delete/', views.UserDeleteView.as_view(), name='user-delete'),
    path('about/', views.about_view, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]