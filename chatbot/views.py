from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import ChatMessageForm
from .models import ChatMessage
from openai import OpenAI
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

def home_view(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ChatMessageForm()
    
    return render(request, 'index.html', {'form': form})

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user'
    
    def get_object(self):
        return self.request.user


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

""" Users """

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'
    login_url = '/login/'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'user_form.html'
    success_url = reverse_lazy('users')

    def test_func(self):
        return self.request.user == self.get_object()
class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = 'user_create.html'
    success_url = reverse_lazy('users')

    def form_valid(self, form):
        # Guardar el usuario con contraseña encriptada
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('users')
    context_object_name = 'user'