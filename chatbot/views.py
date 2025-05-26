from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import ChatMessageForm
from .models import ChatMessage
from openai import OpenAI

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
    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        if new_username:
            user.username = new_username
        if new_email:
            user.email = new_email
        user.save()
    return render(request, 'profile.html', {'user': user})


def chat_view(request):
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            # Creamos instancia sin guardar aún user ni response
            chat = form.save(commit=False)
            chat.user = request.user
            chat.save()
            client = OpenAI()
            # Llamada a OpenAI
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user",   "content": chat.message},
                ],
            )
            chat.response = resp.choices[0].message.content.strip()
            chat.save()

            return redirect('chat')
    else:
        form = ChatMessageForm()

    messages = ChatMessage.objects.select_related('user').order_by('timestamp')
    return render(request, "chat.html", {
        'form': form,
        'messages': messages,
    })

def users_view(request):
    users = User.objects.all() 

    return render(request, 'users.html', {'users': users})

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
