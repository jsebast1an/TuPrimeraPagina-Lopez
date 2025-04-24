from django.shortcuts import render, redirect
from .forms import ChatMessageForm

""" def index(request):
    return render(request, 'index.html') """

def chat_view(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # redirige a la misma vista (o donde quieras)
    else:
        form = ChatMessageForm()
    
    return render(request, 'index.html', {'form': form})