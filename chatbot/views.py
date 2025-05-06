from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ChatMessageForm
# views.py
""" def index(request):
    return render(request, 'index.html') """

def home_view(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # redirige a la misma vista (o donde quieras)
    else:
        form = ChatMessageForm()
    
    return render(request, 'index.html', {'form': form})

def profile_view(request):

    user = request.user  # Obtiene el usuario actual    
    return render(request, 'profile.html', {'user': user})

def chat_view(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')  # redirige a la misma vista (o donde quieras)
    else:
        form = ChatMessageForm()
    
    return render(request, 'chat.html', {'form': form})

def users_view(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')  # redirige a la misma vista (o donde quieras)
    else:
        form = ChatMessageForm()
    
    return render(request, 'users.html', {'form': form})

def about_view(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')  # redirige a la misma vista (o donde quieras)
    else:
        form = ChatMessageForm()
    
    return render(request, 'about.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
