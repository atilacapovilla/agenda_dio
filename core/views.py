from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from core.models import Evento

# def index(request): 
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
   
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    # retorna todos os eventos
    # evento = Evento.objects.all()

    # retorna eventos do usuário logado apenas 
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)

    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
